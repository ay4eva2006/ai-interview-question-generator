import time
from utils.json_parser import AIResponseParser


class RetryEngine:

    def __init__(self, max_retries=2):
        self.max_retries = max_retries

    def run(self, llm, prompt):
        last_error = None

        for attempt in range(self.max_retries):
            response = llm.invoke(prompt)

            parsed = AIResponseParser.parse(response.text)

            if "error" not in parsed:
                return parsed

            last_error = parsed
            time.sleep(1)  # small backoff

        return {
            "error": "max_retries_exceeded",
            "last_error": last_error
        }