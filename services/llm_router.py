class LLMRouter:

    def __init__(self, providers):
        """
        providers = [
            gemini_client,
            groq_client,
            openrouter_client
        ]
        """
        self.providers = providers

    def invoke(self, prompt):
        last_error = None

        for provider in self.providers:
            try:
                response = provider.invoke(prompt)

                if response and response.text:
                    return response

            except Exception as e:
                last_error = str(e)
                continue

        raise Exception(f"All providers failed: {last_error}")