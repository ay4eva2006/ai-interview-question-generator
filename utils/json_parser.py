import re
import json


class AIResponseParser:

    @staticmethod
    def parse(response_text: str):

        if not response_text:
            return {"error": "empty_response"}

        cleaned = response_text.strip()

        # remove markdown
        cleaned = cleaned.replace("```json", "").replace("```", "").strip()

        # 🔥 FIX: collapse broken line breaks inside JSON strings
        cleaned = re.sub(r'\n(?=(?:[^"]*"[^"]*")*[^"]*$)', ' ', cleaned)

        try:
            return json.loads(cleaned)

        except json.JSONDecodeError:
            return {
                "error": "invalid_json",
                "raw_output": cleaned
            }