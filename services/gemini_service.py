import os
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def generate_ai_questions(job_title):

    prompt = f"""
    You are a senior HR interviewer.

    Generate exactly 3 interview questions for a {job_title} role.
    2 technical and 1 behavioral.
    Number them.
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        print("GEMINI ERROR:", e)
        return "Failed to generate questions"