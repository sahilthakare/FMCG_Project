from sklearn.feature_extraction.text import TfidfVectorizer

def vectorize_columns(df, columns, max_features=1000):
    from utils import preprocess_text
    for col in columns:
        df[col + '_processed'] = df[col].apply(preprocess_text)
    combined_text = df[[col + '_processed' for col in columns]].agg(' '.join, axis=1)
    vectorizer = TfidfVectorizer(max_features=max_features)
    tfidf_matrix = vectorizer.fit_transform(combined_text)
    return vectorizer, tfidf_matrix, combined_text
