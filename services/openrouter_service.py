import os

from openai import OpenAI


client = OpenAI(

    api_key=os.getenv("OPENROUTER_API_KEY"),

    base_url="https://openrouter.ai/api/v1"
    

)


def generate_openrouter_questions(job_title):

    try:

        response = client.chat.completions.create(

            model="openrouter/auto-learn-free",

            messages=[
                {
                    "role": "user",
                    "content":
                    f"Generate 3 interview questions for {job_title}"
                }
            ],

            extra_headers={
                "HTTP-Referer": "http://localhost:5000",
                "X-Title": "AI Interview Generator"
                }

        )

        return response.choices[0].message.content

    except Exception as e:

        print("OPENROUTER ERROR:", e)

        return None