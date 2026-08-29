import streamlit as st
import pickle
import string
import nltk

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


# ---------------------------------------------------
# Page configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="SMS Spam Detection",
    page_icon="📱",
    layout="centered"
)


# ---------------------------------------------------
# Download required NLTK resources
# ---------------------------------------------------

@st.cache_resource
def download_nltk_data():
    nltk.download("punkt")
    nltk.download("punkt_tab")
    nltk.download("stopwords")


download_nltk_data()


# ---------------------------------------------------
# Text preprocessing
# ---------------------------------------------------

ps = PorterStemmer()


def transform_text(text):

    text = text.lower()

    # Tokenization
    text = nltk.word_tokenize(text)

    # Keep alphanumeric tokens
    y = []

    for word in text:
        if word.isalnum():
            y.append(word)

    # Remove stopwords and punctuation
    text = y[:]
    y.clear()

    for word in text:
        if word not in stopwords.words("english") and word not in string.punctuation:
            y.append(word)

    # Stemming
    text = y[:]
    y.clear()

    for word in text:
        y.append(ps.stem(word))

    return " ".join(y)


# ---------------------------------------------------
# Load trained model and TF-IDF vectorizer
# ---------------------------------------------------

@st.cache_resource
def load_models():

    with open("vectorizer.pkl", "rb") as file:
        tfidf = pickle.load(file)

    with open("model.pkl", "rb") as file:
        model = pickle.load(file)

    return tfidf, model


tfidf, model = load_models()


# ---------------------------------------------------
# Application UI
# ---------------------------------------------------

st.title("📱 SMS Spam Detection")

st.write(
    "Enter an SMS message below and the machine learning model "
    "will classify it as **Spam** or **Not Spam**."
)

st.divider()


# ---------------------------------------------------
# Input
# ---------------------------------------------------

input_sms = st.text_area(
    "Enter your message",
    placeholder="Example: Congratulations! You have won a free prize...",
    height=150
)


# ---------------------------------------------------
# Prediction
# ---------------------------------------------------

if st.button("🔍 Predict", use_container_width=True):

    if input_sms.strip() == "":
        st.warning("Please enter an SMS message first.")

    else:

        # 1. Preprocess
        transformed_sms = transform_text(input_sms)

        # 2. TF-IDF vectorization
        vector_input = tfidf.transform([transformed_sms])

        # 3. Prediction
        result = model.predict(vector_input)[0]

        st.divider()

        # 4. Display result
        if result == 1:
            st.error("🚨 SPAM MESSAGE")

            st.write(
                "This message has been classified as **Spam**."
            )

        else:
            st.success("✅ NOT SPAM")

            st.write(
                "This message has been classified as **Not Spam**."
            )
