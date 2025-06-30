# FMCG_Project

# 📊 AI-Powered QA System for FMCG Forecasting

This project is an open-source **AI-powered question answering system** designed to intelligently answer user queries using FMCG forecasting and operational data stored in Excel files. It combines classical information retrieval (TF-IDF + cosine similarity) with a lightweight open-source LLM to generate **human-like paragraph answers**, served through a simple **Streamlit interface**.

---

## 🏗️ System Architecture

---------------------------------------------------------------------------------------------------
a. FMCG_PROJECT/: Main project directory.

b. Data/: Contains the input Excel files: Forcast.xlsx, Updated_Main_Data.xlsx

c. src/: Contains source code modules:
1. - __init__.py – Initializes the package
2. - data_loader.py – Loads and cleans Excel data
3. - vectorizer.py – Implements TF-IDF vectorization
4. - retriever.py – Computes cosine similarity for retrieval
5. - llm_answer.py – Generates paragraph-style answers using an open-source LLM
6. - utils.py – Common preprocessing utilities

d. streamlit_app.py: Main Streamlit UI for document upload and answering user queries.

e. requirements.txt: Lists all required Python packages and dependencies.

f. README.md: Provides an overview, setup instructions, and usage guide for the project.



Execution Flow:
1. Document Upload + Query Input  →  streamlit_app.py
2. Data Loading & Cleaning        →  src/data_loader.py
3. Vectorization                  →  src/vectorizer.py
4. Document Retrieval             →  src/retriever.py
5. LLM-based Answer Generation    →  src/llm_answer.py

Note : stewart.ipynb for practise
