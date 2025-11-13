#!/bin/bash
source venv/bin/activate
echo "✅ Virtual environment activated"
pip install -r requirements.txt
echo "🚀 Starting Flask app..."
python app.py


