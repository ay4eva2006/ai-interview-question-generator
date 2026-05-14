import os

from openai import OpenAI



print(os.getenv("GROQ_API_KEY"))


client = OpenAI(

    api_key=os.getenv("GROQ_API_KEY"),

    base_url="https://api.groq.com/openai/v1"

)


def generate_groq_questions(job_title):

    prompt = f"""
    Generate exactly 3 interview questions for a {job_title} role.
    2 technical and 1 behavioral.
    """

    try:

        response = client.chat.completions.create(

            model="llama3-8b-8192",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        )

        return response.choices[0].message.content

    except Exception as e:

        print("GROQ ERROR:", e)

        return None