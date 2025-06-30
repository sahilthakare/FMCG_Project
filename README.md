# FMCG_Project

# 📊 AI-Powered QA System for FMCG Forecasting

This project is an open-source **AI-powered question answering system** designed to intelligently answer user queries using FMCG forecasting and operational data stored in Excel files. It combines classical information retrieval (TF-IDF + cosine similarity) with a lightweight open-source LLM to generate **human-like paragraph answers**, served through a simple **Streamlit interface**.

---

## 🏗️ System Architecture
----------------------------------------------------------------------------------------------------

┌──────────────────────────────┐
│ Document Upload + Query Input│
└────────────┬─────────────────┘
▼
┌──────────────────────────────┐
│ Data Loader (Excel Parser) │
│ └── src/data_loader.py │
└────────────┬─────────────────┘
▼
┌──────────────────────────────┐
│ TF-IDF Vectorizer + Retriever│
│ └── src/vectorizer.py │
│ └── src/retriever.py │
└────────────┬─────────────────┘
▼
┌──────────────────────────────┐
│ LLM-Based Answer Generator │
│ └── src/llm_answer.py │
└────────────┬─────────────────┘

----------------------------------------------------------------------------------------------------


    FMCG_PROJECT/
│
├── Data/
│   └── Forcast.xlsx
│   └── Updated_Main_Data.xlsx
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py         # For loading and cleaning data
│   ├── vectorizer.py          # TF-IDF logic
│   ├── retriever.py           # Cosine similarity logic
│   ├── llm_answer.py          # LLM for paragraph-style answering
│   └── utils.py               # Reusable preprocessing utilities
│
├── streamlit_app.py           # Streamlit UI app
├── requirements.txt
└── README.md

**Note : stewart.ipynb for practise**

