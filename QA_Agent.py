import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def answer_question(query, tfidf_forecast, tfidf_main, df_forecast, df_main, preprocess_text):
    processed_query = preprocess_text(query)
    vector_forecast = tfidf_forecast.transform([processed_query])
    vector_main = tfidf_main.transform([processed_query])
    
    forecast_scores = cosine_similarity(vector_forecast, tfidf_forecast.transform(df_forecast['combined_processed'])).flatten()
    main_scores = cosine_similarity(vector_main, tfidf_main.transform(df_main['combined_processed'])).flatten()
    
    if forecast_scores.max() > 0.3:
        idx = np.argmax(forecast_scores)
        return "📘 **Forecast Data Match**", df_forecast.iloc[idx]
    elif main_scores.max() > 0.3:
        idx = np.argmax(main_scores)
        return "📗 **Main Data Match**", df_main.iloc[idx]
    else:
        return "⚠️ No relevant answer found.", None
