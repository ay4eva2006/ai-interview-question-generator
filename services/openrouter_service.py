import os

from openai import OpenAI

from services.prompt_builder import build_interview_prompt


client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


def generate_openrouter_questions(job_title):

    prompt = build_interview_prompt(job_title)

    try:

        response = client.chat.completions.create(

            model="meta-llama/llama-3.1-8b-instruct:free",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            extra_headers={
                "HTTP-Referer": "http://localhost:5000",
                "X-Title": "AI Interview Generator"
            }

        )

        content = response.choices[0].message.content

        if not content:
            return None

        return content.strip()

    except Exception as e:

        print("OPENROUTER ERROR:", e)

        return None