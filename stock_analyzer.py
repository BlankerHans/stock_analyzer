import numpy as np, pandas as pd, streamlit as st, matplotlib.pyplot as plt

st.set_page_config(
    page_title="Stock Analyzer",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.header("Stock Analyzer 🧮")
st.text("Diese Seite ist eine in Python erstellte Webapplikation zur Analyse von Aktien.")
st.text("Für weiter Informationen klicken Sie hier")

set = pd.DataFrame(data=[50, 400, 20, 75, 38], columns=["Umsatz pro Tag"])
st.bar_chart(set)



