import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import streamlit as st

@st.cache_resource
def load_model():
    df = pd.read_csv("youtube_comments.csv")
    df['label'] = df['label'].astype(str).str.lower().str.strip()
    model = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('cls', LogisticRegression(max_iter=1000))
    ])
    model.fit(df['comment'], df['label'])
    return model

model = load_model()

st.title("Youtube Comment Classifier")
st.write("Classify your comment as toxic or supportive")
user_input = st.text_area("Enter a youtube comment")

if user_input:
    prediction = model.predict([user_input])[0]

    if prediction.lower() == "toxic":
        st.error("Looks like your comment is toxic ❌")
    else:
        st.success("Your comment looks supportive ✅")
