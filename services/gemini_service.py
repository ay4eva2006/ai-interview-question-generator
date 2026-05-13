import os
import time
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def generate_ai_questions(job_title):

    prompt = f"""
    You are a senior HR interviewer.

    Generate exactly 3 interview questions for a {job_title} role.

    Requirements:
    - 2 technical questions
    - 1 behavioral question
    - concise
    - numbered list only
    """

    for i in range(3):
        try:
            model = genai.GenerativeModel("gemini-1.5-flash")

            response = model.generate_content(prompt)

            return response.text

        except Exception as e:
            print(f"Retrying... attempt {i+1}")
            time.sleep(2)

    return None