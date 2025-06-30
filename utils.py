import string
import nltk
from nltk.corpus import stopwords
import pandas as pd

nltk.download('stopwords')

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    if isinstance(text, str):
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        text = ' '.join([word for word in text.split() if word not in stop_words])
        return text
    return ""

def prepare_dataframe(df, text_columns):
    for col in text_columns:
        df[col + '_processed'] = df[col].apply(preprocess_text)
    combined_col = 'combined_processed'
    df[combined_col] = df[text_columns[0] + '_processed'] + " " + df[text_columns[1] + '_processed']
    return df
