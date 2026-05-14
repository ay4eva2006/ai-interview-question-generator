import os

from google import genai
from dotenv import load_dotenv


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_ai_questions(job_title):

    prompt = f"""
    Generate exactly 3 interview questions
    for a {job_title} role.
    """

    try:

        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        print("GEMINI ERROR:", e)

        return None