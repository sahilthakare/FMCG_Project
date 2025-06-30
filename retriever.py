from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def retrieve_most_similar_row(query, vectorizer, tfidf_matrix, combined_texts, df):
    from utils import preprocess_text
    processed_query = preprocess_text(query)
    query_vec = vectorizer.transform([processed_query])
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    best_index = np.argmax(similarities)
    best_score = similarities[best_index]
    if best_score < 0.3:
        return None, 0
    return df.iloc[best_index], best_score
