import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load saved models and vectorizer
knn_model = joblib.load("knn_model.pkl")
svm_model = joblib.load("svm_model.pkl")
rf_model = joblib.load("rf_model.pkl")
tfidf_vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Preprocessing function
def preprocess_text(text):
    import string
    import re
    from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

    # Initialize stemmer
    stemmer = StemmerFactory().create_stemmer()

    # Text cleaning
    text = text.lower()
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = stemmer.stem(text)  # Stemming
    return text

# Function to classify new data
def classify_text(model, vectorizer, text):
    preprocessed_text = preprocess_text(text)
    vectorized_text = vectorizer.transform([preprocessed_text])
    prediction = model.predict(vectorized_text)
    return prediction[0]

# Example usage
new_text = "Merek Mobil Nasional Malaysia Luncurkan Mobil Listrik Pertama"  # Replace with new text
tfidf_vectorizer

print("KNN Prediction:", classify_text(knn_model, tfidf_vectorizer, new_text))
print("SVM Prediction:", classify_text(svm_model, tfidf_vectorizer, new_text))
print("Random Forest Prediction:", classify_text(rf_model, tfidf_vectorizer, new_text))