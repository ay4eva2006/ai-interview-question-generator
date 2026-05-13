import unittest
from unittest.mock import patch

from services.gemini_service import \
    generate_ai_questions


class TestGeminiService(unittest.TestCase):

    @patch(
        "services.gemini_service.client.models.generate_content"
    )
    def test_generate_ai_questions(
        self,
        mock_generate
    ):

        mock_generate.return_value.text = \
            "1. Question"

        result = generate_ai_questions(
            "Software Engineer"
        )

        self.assertIn(
            "1. Question",
            result
        )


if __name__ == "__main__":
    unittest.main()