#!/bin/bash

echo "🧪 Running Shortcut Lifecycle Validation..."
python3 validate_shortcut_lifecycle.py

echo "🔗 Running Notion Sync..."
export NOTION_TOKEN="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"
export NOTION_DATABASE_ID="1cfbd31f04638042ad6febc73988991e"
bash run_notion_sync.sh

echo "🚀 Launching Streamlit Dashboard..."
streamlit run main_app.py
