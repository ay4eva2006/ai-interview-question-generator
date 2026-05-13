import unittest

from utils.validators import validate_job_title


class TestValidators(unittest.TestCase):

    def test_empty_job_title(self):

        result = validate_job_title("")

        self.assertEqual(
            result,
            "Job title is required"
        )

    def test_short_job_title(self):

        result = validate_job_title("abc")

        self.assertEqual(
            result,
            "Please enter a valid job title"
        )

    def test_invalid_job_title(self):

        result = validate_job_title("12345")

        self.assertEqual(
            result,
            "Please enter a valid job title"
        )

    def test_unrecognized_job_title(self):

        result = validate_job_title("wizard")

        self.assertEqual(
            result,
            "Please enter a recognizable job title"
        )

    def test_valid_job_title(self):

        result = validate_job_title(
            "Software Engineer"
        )

        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()