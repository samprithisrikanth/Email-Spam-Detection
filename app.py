import streamlit as st
import pickle
import nltk
import string

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download stopwords
nltk.download('stopwords')

# Create stemmer object
ps = PorterStemmer()

# Text preprocessing function
def transform_text(text):

    # Convert to lowercase
    text = text.lower()

    # Split into words
    text = text.split()

    # Remove stopwords and punctuation
    filtered_words = []

    for word in text:
        if word not in stopwords.words('english') and word not in string.punctuation:
            filtered_words.append(word)

    # Apply stemming
    stemmed_words = []

    for word in filtered_words:
        stemmed_words.append(ps.stem(word))

    # Join words back into sentence
    return " ".join(stemmed_words)

# Load saved model and vectorizer
model = pickle.load(open('spam_model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Page configuration
st.set_page_config(
    page_title="Spam Detection System",
    layout="centered"
)

# Custom CSS Styling
st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        rgba(5, 10, 15, 0.92),
        rgba(15, 20, 25, 0.96)
    ),
    url("https://images.unsplash.com/photo-1526378800651-cf1f6f7f2d0c?q=80&w=2070&auto=format&fit=crop");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: #f5f5f5;
}

.main-title {
    font-size: 44px;
    font-weight: bold;
    text-align: center;
    color: #d4af37;
    margin-top: 20px;
    letter-spacing: 2px;
    font-family: serif;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #cccccc;
    margin-bottom: 35px;
    font-family: serif;
}

textarea {
    background-color: rgba(15,15,15,0.88) !important;
    color: white !important;
    border-radius: 14px !important;
    border: 1px solid #d4af37 !important;
    font-size: 16px !important;
    padding: 12px !important;
}

.stButton>button {
    width: 100%;
    background-color: rgba(20,20,20,0.9);
    color: #d4af37;
    border: 1px solid #d4af37;
    border-radius: 12px;
    height: 3em;
    font-size: 18px;
    transition: 0.3s ease;
}

.stButton>button:hover {
    background-color: #d4af37;
    color: black;
}

.result-box {
    padding: 20px;
    border-radius: 15px;
    background-color: rgba(20,20,20,0.88);
    border: 1px solid #d4af37;
    margin-top: 25px;
    text-align: center;
    font-size: 24px;
    font-family: serif;
    color: white;
    box-shadow: 0px 0px 20px rgba(212,175,55,0.2);
}

.footer {
    text-align: center;
    margin-top: 40px;
    color: #aaaaaa;
    font-size: 14px;
    font-family: serif;
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown(
    '<div class="main-title">Spam Detection System</div>',
    unsafe_allow_html=True
)

# Subtitle
st.markdown(
    '<div class="subtitle">Machine Learning Powered Email Security Analyzer</div>',
    unsafe_allow_html=True
)

# Input area
message = st.text_area(
    "Enter Email or Message",
    height=200,
    placeholder="Type your email or message here..."
)

# Prediction button
if st.button("Analyze Message"):

    if message.strip() != "":

        # Preprocess text
        processed_message = transform_text(message)

        # Convert into vector
        transformed_message = vectorizer.transform([processed_message])

        # Prediction
        prediction = model.predict(transformed_message)

        # Probability score
        probability = model.predict_proba(transformed_message)

        confidence = probability.max() * 100

        # Result display
        if prediction[0] == 1:

            st.markdown(
                f'''
                <div class="result-box">
                    Spam Message Detected
                    <br><br>
                    Confidence Score: {confidence:.2f}%
                </div>
                ''',
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f'''
                <div class="result-box">
                    Message Appears Safe
                    <br><br>
                    Confidence Score: {confidence:.2f}%
                </div>
                ''',
                unsafe_allow_html=True
            )

    else:
        st.warning("Please enter a message.")

# Footer
st.markdown(
    '<div class="footer">Analyze. Detect. Protect.</div>',
    unsafe_allow_html=True
)
    