import streamlit as st

from data_loader import load_excel_data
from vectorizer import vectorize_columns
from retriever import retrieve_most_similar_row
from llm_answer import generate_answer

st.set_page_config(page_title="FMCG QA Agent", layout="wide")
st.title("🧠 AI-Powered FMCG Document QA Agent")

uploaded_forecast = st.file_uploader("Upload Forecast Excel File", type=["xlsx"])
uploaded_main = st.file_uploader("Upload Main Data Excel File", type=["xlsx"])

if uploaded_forecast and uploaded_main:
    df_forecast, df_main = load_excel_data(uploaded_forecast, uploaded_main)

    forecast_cols = ['Product description', 'STATUS']
    main_cols = ['Name', 'Item Description']

    vec_forecast, mat_forecast, combined_forecast = vectorize_columns(df_forecast, forecast_cols)
    vec_main, mat_main, combined_main = vectorize_columns(df_main, main_cols)

    question = st.text_input("Ask your question:")
    if question:
        row_forecast, score_forecast = retrieve_most_similar_row(question, vec_forecast, mat_forecast, combined_forecast, df_forecast)
        row_main, score_main = retrieve_most_similar_row(question, vec_main, mat_main, combined_main, df_main)

        if score_forecast > score_main and row_forecast is not None:
            context = row_forecast.to_string()
        elif row_main is not None:
            context = row_main.to_string()
        
        else:
            st.warning("⚠️ Sorry, I could not find relevant information.")
            context = ""
        

        if context:
            answer = generate_answer(question, context)
            st.markdown("### 🤖 Answer:")
            st.write(answer)
