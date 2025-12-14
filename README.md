# sms-spam-detection
SMS Spam Detection using Machine Learning

PROJECT OVERVIEW:

This project focuses on building a machine learning–based SMS Spam Detection system that classifies messages as Spam or Ham (Not Spam).
Natural Language Processing (NLP) techniques are used to preprocess text data, followed by feature extraction and model training to achieve accurate classification.

OBJECTIVES:

* To clean and preprocess raw SMS text data

* To perform exploratory data analysis (EDA) to understand message patterns

* To convert text into numerical features using TF-IDF

* To train and evaluate multiple machine learning classifiers

* To identify the best-performing model for spam detection

DATASET:

* Dataset contains SMS messages labeled as spam or ham

* Columns include:

1) Message text

2) Target label (Spam / Ham)

PROJECT WORKFLOW:

1) Data Cleaning:

* Removed unnecessary columns

* Handled missing values

* Renamed columns for clarity

* Encoded target labels

2) Exploratory Data Analysis (EDA): 

* Distribution of spam vs ham messages

* Analysis of message length, word count, and character count

* Correlation analysis using heatmaps

* Visualization using histograms and pair plots

3) Text Preprocessing :

* Converted text to lowercase

* Tokenization

* Removal of special characters and punctuation

* Stopword removal

* Stemming

4) Feature Extraction :

* Used TF-IDF Vectorizer to transform text data into numerical features

5) Model Building :

* Trained machine learning models such as:

    * Naive Bayes

    * Logistic Regression

    * Support Vector Machine (SVM)

* Compared model performance

6) Model Evaluation :

* Accuracy score

* Precision

* Confusion Matrix

BEST MODEL PERFORMANCE :

* Multinomial Naive Bayes achieved high precision and accuracy

* Particularly effective in minimizing false positives for spam messages

TECHNOLOGIES USED :

* Programming Language: Python

* Libraries:

    * NumPy

    * Pandas

    * Matplotlib

    * Seaborn

    * Scikit-learn

    * NLTK

RESULTS :

* Successfully classified SMS messages as spam or ham

* Achieved strong precision, making the model suitable for real-world spam filtering systems

CONCLUSION :

This project demonstrates the complete NLP pipeline—from raw text preprocessing to model evaluation—for solving a real-world classification problem.
It highlights the effectiveness of traditional machine learning models in text-based spam detection tasks.
