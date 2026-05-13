from google import genai
from dotenv import load_dotenv

import os
import time

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_ai_questions(job_title):

    prompt = f"""
    You are a senior HR interviewer.

    Generate exactly 3 interview
    questions for a {job_title} role.

    Requirements:
    - 2 technical questions
    - 1 behavioral questions
    - concise
    - numbered list only
    """

    response = None

    for i in range(3):

        try:

            response = \
                client.models.generate_content(

                model="models/gemini-flash-latest",

                contents=prompt
            )

            break

        except Exception as e:

            print(
                f"Retrying... attempt {i+1}"
            )

            time.sleep(2)

    if not response:

        return None

    return response.text