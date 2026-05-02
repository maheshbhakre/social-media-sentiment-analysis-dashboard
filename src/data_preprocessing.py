import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\\S+', '', text)
    text = re.sub(r'[^a-zA-Z\\s]', '', text)

    text = " ".join([
        word for word in text.split()
        if word not in stop_words
    ])

    return text

df = pd.read_csv('../data/social_media_data.csv')

df['cleaned_text'] = df['text'].apply(clean_text)

df.to_csv('../data/cleaned_data.csv', index=False)

print(df.head())

print("Preprocessing Completed")