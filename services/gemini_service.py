import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Setup for google-generativeai (the library you have installed)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_ai_questions(job_title):
    prompt = f"""
    You are a senior HR interviewer.

    Generate exactly 3 interview questions for a {job_title} role.
    2 technical and 1 behavioral.
    Number them.
    """

    try:
        # Use GenerativeModel instead of Client
        # Note: Changed to 'gemini-1.5-flash' as '2.5' does not exist yet
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        print("GEMINI ERROR:", e)
        return "Failed to generate questions"