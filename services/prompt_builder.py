def build_interview_prompt(job_title):
    return f"""
### ROLE
You are a Professional HR Auditor. 

### MANDATORY VALIDATION RULE
Before generating anything, determine if "{job_title}" is a real-world, taxable professional occupation found in a database like LinkedIn or O*NET.
- If "{job_title}" is a joke, a hobby, an inanimate object, a fictional character (e.g., Couch Potato, Batman, Pizza), you MUST NOT generate questions.
- If invalid, respond with EXACTLY and ONLY this word: [WRONG JOB DESRIPTION]

### GENERATION RULES (ONLY IF VALID)
1. Generate exactly 3 professional interview questions.
2. Format: Output exactly 3 paragraphs. 
3. NO numbers, NO bullet points, NO intro text, NO labels like "Technical:".
4. Separation: Put two "Enter" keys (double newline) between every paragraph.
5. Do not break a single sentence into multiple lines.nput Correct Job Title.


{{
  "job_title": "{job_title}",
  "questions": [
    {{
      "type": "technical",
      "question": "string"
    }},
    {{
      "type": "behavioral",
      "question": "string"
    }},
    {{
      "type": "situational_judgment",
      "question": "string"
    }}
  ]
}}

USER INPUT: {job_title}
"""