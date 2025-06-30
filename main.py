import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

from utils import preprocess_text, prepare_dataframe
from QA_Agent import answer_question

st.set_page_config(page_title="FMCG QA Agent", layout="wide")
st.title("🧠 AI-Powered Document QA Agent for FMCG Data")

# Upload Files
uploaded_forecast = st.file_uploader("Upload Forecast Excel File", type=['xlsx'])
uploaded_main = st.file_uploader("Upload Main Excel File", type=['xlsx'])

if uploaded_forecast and uploaded_main:
    df_forecast = pd.read_excel(uploaded_forecast)
    df_main = pd.read_excel(uploaded_main)

    # Define relevant columns
    forecast_cols = ['Product description', 'STATUS']
    main_cols = ['Name', 'Item Description']

    # Preprocess and combine
    df_forecast = prepare_dataframe(df_forecast, forecast_cols)
    df_main = prepare_dataframe(df_main, main_cols)

    # Fit TF-IDF
    tfidf_forecast = TfidfVectorizer(max_features=1000).fit(df_forecast['combined_processed'])
    tfidf_main = TfidfVectorizer(max_features=1000).fit(df_main['combined_processed'])

    st.success("✅ Files processed and ready for Q&A")

    # User input
    user_query = st.text_input("🔎 Ask your question here:")

    if st.button("Get Answer"):
        if user_query:
            title, answer = answer_question(user_query, tfidf_forecast, tfidf_main, df_forecast, df_main, preprocess_text)
            st.markdown(f"### {title}")
            if answer is not None:
                st.dataframe(answer.to_frame().T)
        else:
            st.warning("Please enter a question.")
