# MindShield

### Detecting Suspicious Messages Using NLP & Machine Learning

MindShield is a cybersecurity-focused machine learning project that analyzes emails and messages to identify spam, phishing, and potentially suspicious content using Natural Language Processing (NLP), TF-IDF feature extraction, and machine learning classification.

## Project Overview

MindShield is designed to improve digital communication safety by detecting risky or deceptive message patterns commonly found in:

- Spam emails
- Phishing attempts
- OTP scams
- Banking fraud messages
- Suspicious promotional content

The project combines:
- Machine Learning based prediction
- NLP preprocessing
- Rule-based threat detection
- Streamlit web deployment

## Features

- NLP-based text preprocessing
- Stopwords removal and stemming
- TF-IDF feature extraction
- Spam & phishing classification
- Confidence score prediction
- Hybrid ML + rule-based detection
- Streamlit interactive interface
- Cybersecurity-themed UI

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Streamlit

## Machine Learning Workflow

```text
Data Collection
↓
Data Cleaning
↓
Text Preprocessing (NLP)
↓
Feature Extraction using TF-IDF
↓
Model Training
↓
Prediction & Evaluation
↓
Streamlit Deployment
```

## NLP Techniques Used

- Lowercase conversion
- Tokenization
- Stopwords removal
- Punctuation removal
- Stemming using Porter Stemmer

## Model Information

| Component | Used |
|---|---|
| Vectorization | TF-IDF Vectorizer |
| Classification Model | Logistic Regression |
| NLP Library | NLTK |
| Deployment | Streamlit 

## Project Structure

```text
MindShield/
│
├── app.py
├── spam_detection.ipynb
├── spam_model.pkl
├── vectorizer.pkl
├── spam.csv
├── requirements.txt
└── README.md
```

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Example Detection Types

### Suspicious Messages
- OTP scams
- Banking verification requests
- Credential phishing attempts
- Fake promotional messages

### Safe Messages
- General communication
- Educational messages
- Work-related conversations
- Regular email content

## Future Improvements

- Real-time email scanning
- Threat level categorization
- Dashboard analytics
- Deep learning integration
- Multilingual spam detection
- User authentication system

## Disclaimer

This project is developed for educational and cybersecurity awareness purposes. Predictions may vary depending on message complexity and evolving scam patterns.

## Author

**Samprithi S**

MindShield • Analyze. Detect. Protect.
