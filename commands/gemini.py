import google.generativeai as genai

YOUR_GEMINI_API_KEY = "Your_api_key"
genai.configure(api_key=f"{YOUR_GEMINI_API_KEY}")

model = genai.GenerativeModel("models/gemini-1.5-flash")

def ai_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return "Sorry, I couldn't process that right now."