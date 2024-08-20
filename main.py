import streamlit as st
import pandas as pd
import openai_helper

st.set_page_config(page_title="💸💰 Financial Data Extraction 💸💰", page_icon="💰", layout="wide")

st.markdown("""
    <style>
        .main-container {
            background-color: #f0f2f6;
            padding: 2rem;
        }
        .title-container {
            text-align: center;
            font-size: 2.5rem;
            font-weight: bold;
            color: #007BFF;
        }
        .textarea-container {
            margin-top: 1rem;
        }
        .extract-button {
            background-color: #28a745;
            color: white;
            padding: 0.75rem;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            width: 100%;
        }
        .dataframe-container {
            margin-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)


st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<div class="title-container">💸💰 Financial Data Extraction Tool</div>', unsafe_allow_html=True)


col1, col2 = st.columns([3, 2])

# Default DataFrame
financial_data_df = pd.DataFrame({
    "Measure": ["Company Name", "Stock Symbol", "Revenue", "Net Income", "EPS"],
    "Value": ["", "", "", "", ""]
})

with col1:
    st.markdown('<div class="textarea-container">', unsafe_allow_html=True)
    news_article = st.text_area("Paste your news article here...", height=300,
                                placeholder="Enter or paste the financial news article...")
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Extract", key="extract", help="Click to extract financial data"):
        financial_data_df = openai_helper.extract_financial_data(news_article)

with col2:
    st.markdown('</br><div class="dataframe-container">', unsafe_allow_html=True)
    st.dataframe(
        financial_data_df,
        hide_index=True,
        use_container_width=True,
        column_config={
            "Measure": st.column_config.Column(width=150),
            "Value": st.column_config.Column(width=150)
        }
    )
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
