import streamlit as st
import pandas as pd

def shortcut_dashboard_tab():
    st.title("📊 Shortcut Dashboard")
    df = pd.DataFrame({
        "Shortcut": ["#A", "#M", "#V", "#X"],
        "Status": ["Active", "Active", "Active", "Active"]
    })
    st.dataframe(df)