# 📱 SMS Spam Detection using Machine Learning

A machine learning and **Natural Language Processing (NLP)** project that classifies SMS messages as **Spam** or **Ham (Not Spam)** using text preprocessing, TF-IDF feature extraction, and multiple machine learning classifiers.

## 🚀 Live Streamlit Dashboard

🔗 **Live App:** [Open SMS Spam Detection Dashboard](https://sms-spam-detection-pqyqgltv2duwzub8ugoqik.streamlit.app/)

The interactive Streamlit dashboard provides access to:

* 💬 **SMS Classification** — classify messages as Spam or Ham
* 🧹 **Text Preprocessing** — clean and process raw SMS text
* 📊 **Message Analysis** — explore spam/ham distribution and message patterns
* 🔤 **TF-IDF Feature Extraction** — convert text into numerical features
* 🤖 **Model Comparison** — compare Naive Bayes, Logistic Regression, and SVM
* 📈 **Model Evaluation** — analyze accuracy, precision, and confusion matrix
* 🎯 **Spam Prediction** — test custom SMS messages using the trained model

---

## 📌 Project Overview

This project focuses on building a **machine learning-based SMS Spam Detection system** that classifies messages as **Spam** or **Ham (Not Spam)**.

Natural Language Processing techniques are used to preprocess text data, followed by feature extraction and machine learning model training to achieve effective spam classification.

---

## 🎯 Objectives

* 🧹 Clean and preprocess raw SMS text data
* 📊 Perform Exploratory Data Analysis (EDA) to understand message patterns
* 🔤 Convert text into numerical features using **TF-IDF**
* 🤖 Train and evaluate multiple machine learning classifiers
* 🏆 Compare model performance for spam detection

---

## 📂 Dataset

The dataset contains SMS messages labeled as **Spam** or **Ham**.

### Dataset Columns

* 💬 **Message** — SMS message text
* 🎯 **Target Label** — Spam / Ham

---

## 🔄 Project Workflow

### 1. Data Cleaning

* Removed unnecessary columns
* Handled missing values
* Renamed columns for clarity
* Encoded target labels

### 2. Exploratory Data Analysis

The EDA phase includes:

* 📊 Spam vs Ham message distribution
* 📏 Message length analysis
* 🔢 Word count analysis
* 🔤 Character count analysis
* 🔥 Correlation analysis using heatmaps
* 📈 Histograms and pair plots

### 3. Text Preprocessing

The SMS text was processed using NLP techniques:

* Converted text to lowercase
* Tokenization
* Removal of special characters and punctuation
* Stopword removal
* Stemming

### 4. Feature Extraction

**TF-IDF Vectorization** was used to transform the processed SMS text into numerical feature representations suitable for machine learning models.

### 5. Model Building

The following classifiers were trained and compared:

* 🧮 **Multinomial Naive Bayes**
* 📈 **Logistic Regression**
* 📐 **Support Vector Machine (SVM)**

### 6. Model Evaluation

Models were evaluated using:

* **Accuracy Score**
* **Precision**
* **Confusion Matrix**

---

## 🏆 Best Model Performance

**Multinomial Naive Bayes** achieved high precision and accuracy in the project evaluation.

It was particularly effective for minimizing false-positive spam classifications.

---

## 🛠️ Technologies Used

### Programming Language

* **Python**

### Libraries

* **NumPy**
* **Pandas**
* **Matplotlib**
* **Seaborn**
* **Scikit-learn**
* **NLTK**
* **Streamlit**

---

## 📊 Results

* Successfully classified SMS messages as **Spam** or **Ham**
* Achieved strong precision in spam classification
* Demonstrated the effectiveness of traditional machine learning models for text classification
* Built an interactive Streamlit interface for testing SMS messages

---

## 🏁 Conclusion

This project demonstrates a complete **NLP and machine learning pipeline**, from raw text preprocessing and feature extraction to model training and evaluation.

It highlights how traditional machine learning algorithms combined with **TF-IDF** can be effectively applied to real-world text classification problems such as SMS spam detection.
