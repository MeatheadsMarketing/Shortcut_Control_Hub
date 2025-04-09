import streamlit as st
from tab_notion_sync import notion_sync_tab
from tab_shortcut_lifecycle import shortcut_lifecycle_tab
from tab_shortcut_dashboard import shortcut_dashboard_tab

st.set_page_config(page_title="Shortcut Control Hub", layout="wide")

selected_tab = st.sidebar.selectbox("📂 Shortcut Control Hub", [
    "🔗 Notion Sync",
    "📘 Shortcut Lifecycle",
    "📊 Shortcut Dashboard"
])

if selected_tab == "🔗 Notion Sync":
    notion_sync_tab()
elif selected_tab == "📘 Shortcut Lifecycle":
    shortcut_lifecycle_tab()
elif selected_tab == "📊 Shortcut Dashboard":
    shortcut_dashboard_tab()
