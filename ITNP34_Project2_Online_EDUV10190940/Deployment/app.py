
import streamlit as st
import pandas as pd
import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

# Download NLP resources
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

# Configure application
st.set_page_config(
    page_title="Researchly Research Abstract Classifier",
    layout="wide"
)

st.title("Researchly Research Abstract Classifier")

st.write(
    "This app classifies research abstracts as either "
    "AI-related or classical research."
)

# Initialise text preprocessing
stop_words = set(stopwords.words('english')) - {'no', 'nor', 'not'}
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'<[^>]+>|http\S+|www\S+', ' ', text)
    text = re.sub(r'\S+@\S+', ' ', text)
    text = re.sub(r'\d+', ' ', text)
    text = re.sub(r'[^a-z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()

    words = text.split()

    words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word not in stop_words and len(word) > 2
    ]

    return ' '.join(words)

# Train the Random Forest model
@st.cache_resource
def train_model():

    df = pd.read_json('research_abstracts.json')

    abstract_col = next(
        col for col in df.columns if 'abstract' in col.lower()
    )

    df = df.dropna(subset=[abstract_col, 'Label']).copy()

    df['cleaned_abstract'] = df[abstract_col].apply(clean_text)

    df = df[df['cleaned_abstract'] != ''].copy()
    df = df.drop_duplicates(subset=['cleaned_abstract'])

    model = Pipeline([
        ('tfidf', TfidfVectorizer(
            max_features=1000,
            ngram_range=(1, 2)
        )),
        ('classifier', RandomForestClassifier(
            n_estimators=300,
            class_weight='balanced',
            random_state=42
        ))
    ])

    model.fit(df['cleaned_abstract'], df['Label'])

    return model

model = train_model()

# Abstract input
abstract = st.text_area(
    "Enter research abstract:",
    height=160
)

# Classification
if st.button("Classify Abstract"):

    if abstract.strip():

        cleaned = clean_text(abstract)

        if cleaned:
            prediction = model.predict([cleaned])[0]

            st.subheader("Prediction")

            if str(prediction).lower() == 'ai':
                st.success(
                    "The abstract is classified as: "
                    "Artificial Intelligence"
                )
            else:
                st.success(
                    "The abstract is classified as: Classical Research"
                )

            probabilities = model.predict_proba([cleaned])[0]

            st.write(
                "Prediction confidence:",
                f"{max(probabilities) * 100:.2f}%"
            )

            probability_df = pd.DataFrame({
                'Category': model.classes_,
                'Probability (%)': probabilities * 100
            })

            st.bar_chart(
                probability_df.set_index('Category')
            )

        else:
            st.warning("Please enter a valid research abstract.")

    else:
        st.warning("Please enter a research abstract.")
