# 🧠 Jarvis 2.0 - Python Voice Assistant

**Jarvis 2.0** is an AI-powered modular voice assistant built with Python. It performs real-time tasks via speech such as:

- 🎵 Playing music from a local music library
- 🌐 Opening popular websites (50+ included)
- ☁️ Fetching current weather using location-based API
- 📰 Reading top headlines via News API
- 🗂️ Organizing your files by type into folders
- 📸 Taking pictures using webcam
- 💬 Sending WhatsApp messages through speech
- 🤖 AI-powered responses using Gemini API

---

## 🔧 Features

- **Voice-activated with wake word** ("Jarvis")
- **Modular structure** using multiple `.py` files for each task
- **Speech recognition and text-to-speech** using `speech_recognition` and `pyttsx3`
- **API integration** with NewsAPI, Visual Crossing Weather, Google Gemini AI
- Easily extendable for reminders, emails, or desktop automation

---

## 📦 Requirements

Install dependencies:
This project uses several free APIs. Before running the assistant, you need to generate the following keys:

Feature	API Provider	Website
🌦️ Weather	Visual Crossing	https://www.visualcrossing.com/
📰 News Headlines	NewsAPI	https://newsapi.org/
🤖 AI Chat	Google Gemini AI	https://aistudio.google.com/app/apikey

Once you sign up and generate your API keys, open the relevant .py files (e.g., weather.py, news.py, ai_chat.py) and replace the string:
YOUR_GEMINI_API_KEY/ WEATHER_API_KEY/ NEWS_API_KEY = "your_api_key"   # Replace this with your actual API key

Install the required modules using:
```bash
pip install -r requirement.txt

