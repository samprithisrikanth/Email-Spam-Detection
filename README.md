# Email Spam Detection System 
An AI-based **Machine Learning project** that uses Natural Language Processing (NLP) to determine whether an email is Spam or Not Spam using the Naive Bayes Classifier.

## Features
- Text processing (NLP)
- Stopwords elimination and stemming
- Features extracted using CountVectorizer
- ML model: Multinomial Naive Bayes
- Web app interface using Streamlit
- Predicts confidence scores

## Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- NLTK
- Streamlit

## Workflow
Data → Data Cleaning → NLP → Feature Extraction → ML Model Training → Prediction → Streamlit Interface

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
