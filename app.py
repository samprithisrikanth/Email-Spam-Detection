import streamlit as st
import pickle
import nltk
import string

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download stopwords
nltk.download('stopwords')

# Stemmer
ps = PorterStemmer()

# Store stopwords once
stop_words = set(stopwords.words('english'))

# Text preprocessing function

def transform_text(text):

    text = str(text).lower()

    words = text.split()

    filtered_words = []

    for word in words:
        if word not in stop_words and word not in string.punctuation:
            filtered_words.append(word)

    stemmed_words = []

    for word in filtered_words:
        stemmed_words.append(ps.stem(word))

    return " ".join(stemmed_words)

# Load model and vectorizer
model = pickle.load(open('spam_model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Page settings
st.set_page_config(
    page_title="MindShield",
    layout="centered"
)

# ---------- CUSTOM CSS ----------

st.markdown("""
<style>

.stApp {
    background:
    linear-gradient(rgba(10,12,16,0.95), rgba(18,22,28,0.96)),
    url('https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=2070&auto=format&fit=crop');

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 700;
    color: #e6d3a3;
    letter-spacing: 1px;
    margin-bottom: 10px;
    font-family: Georgia, serif;
}

.subtitle {
    text-align: center;
    color: #b8bcc5;
    font-size: 16px;
    margin-bottom: 35px;
}

.description-box {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 16px;
    border-radius: 14px;
    color: #c9ced8;
    font-size: 15px;
    margin-bottom: 25px;
}

textarea {
    background-color: rgba(12,15,20,0.92) !important;
    color: #f5f5f5 !important;
    border-radius: 12px !important;
    border: 1px solid rgba(230,211,163,0.25) !important;
    font-size: 16px !important;
    padding: 14px !important;
}

.stButton > button {
    width: 100%;
    height: 3.2rem;
    border-radius: 12px;
    border: none;
    background: #d9c089;
    color: black;
    font-size: 16px;
    font-weight: 600;
    transition: 0.25s ease;
}

.stButton > button:hover {
    background: #f0d79c;
}

.result-card {
    margin-top: 25px;
    padding: 22px;
    border-radius: 16px;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    text-align: center;
    backdrop-filter: blur(4px);
}

.result-title {
    font-size: 24px;
    font-weight: 600;
    color: #ffffff;
    margin-bottom: 10px;
}

.result-subtitle {
    font-size: 15px;
    color: #c5cad3;
}

.footer {
    text-align: center;
    margin-top: 50px;
    color: #8f96a3;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------

st.markdown(
    '<div class="main-title">MindShield</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your Inbox Has a Security System Now</div>',
    unsafe_allow_html=True
)

# ---------- DESCRIPTION ----------

st.markdown(
    '''
    <div class="description-box">
    Paste an email, SMS, or suspicious message below to analyze whether the content appears safe or potentially risky.
    </div>
    ''',
    unsafe_allow_html=True
)

# ---------- INPUT ----------

message = st.text_area(
    "Message Content",
    height=220,
    placeholder="Paste your email, SMS, or suspicious text here..."
)

# Rule-based security keywords
suspicious_keywords = [
    "otp",
    "bank account",
    "cvv",
    "atm",
    "debit card",
    "credit card",
    "screenshot",
    "verify account",
    "bank details"
]

message_lower = message.lower()

rule_based_spam = any(keyword in message_lower for keyword in suspicious_keywords)

# ---------- BUTTON ----------

if st.button("Analyze Message"):

    if message.strip() != "":

        # Preprocess message
        processed_message = transform_text(message)

        # Convert text to vector
        transformed_message = vectorizer.transform([processed_message])

        # Predict
        prediction = model.predict(transformed_message)

        # Confidence score
        probability = model.predict_proba(transformed_message)

        confidence = probability.max() * 100

        # Final spam check
        is_spam = (prediction[0] == 1 or rule_based_spam)

        # ---------- SPAM RESULT ----------

        if is_spam:

            st.error("Potential Threat Detected")

            st.write(f"Confidence Score: {confidence:.2f}%")

            st.caption(
                "This message contains patterns commonly associated with phishing or spam attempts."
            )

            st.progress(float(confidence) / 100)

        # ---------- SAFE RESULT ----------

        else:

            st.success("Message Appears Safe")

            st.write(f"Confidence Score: {confidence:.2f}%")

            st.caption(
                "No suspicious patterns were detected in this message."
            )

            st.progress(float(confidence) / 100)

    else:

        st.warning("Please enter a message before analysis.")