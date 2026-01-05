import unittest
from config import MAX_FILE_READ
from functions.get_file_content import get_file_content


class TestGetFileContent(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_get_file_content_success_with_file_over_10000_char(self):
        file_path = "lorem.txt"
        result = get_file_content("./calculator/", file_path)
        truncated_message = (
            f'[...File "{file_path}" truncated at {MAX_FILE_READ} characters'
        )
        self.assertIsInstance(result, str)
        self.assertNotIn("Error:", result)
        self.assertIn(truncated_message, result)

        self.assertEqual(len(result), MAX_FILE_READ + len(truncated_message))
        print(
            f"Success test result snippet: {result[-(50+len(truncated_message)):]}..."
        )

    def test_get_file_content_success_with_main_py_file(self):
        file_path = "main.py"
        result = get_file_content(".", file_path)

        self.assertIsInstance(result, str)
        self.assertNotIn("Error:", result)

        self.assertTrue(len(result) < MAX_FILE_READ)
        print(f"Success test result snippet: {result[:500]}...")

    def test_get_file_content_success_with_pkg_calculator(self):
        file_path = "pkg/calculator.py"
        result = get_file_content("./calculator/", file_path)

        self.assertIsInstance(result, str)
        self.assertNotIn('"Error:', result)

        self.assertTrue(len(result) < MAX_FILE_READ)
        print(f"Success test result snippet: {result}...")

    def test_get_file_content_success_with_file_under_10000_char(self):
        result = get_file_content("./functions/test_assets/", "test_sample.txt")

        self.assertIsInstance(result, str)
        self.assertNotIn("Error:", result)

        self.assertTrue(len(result) < MAX_FILE_READ)
        print(f"Success test result snippet: {result[-300:]}...")

    def test_get_file_content_not_found(self):
        result = get_file_content(".", "non_existent_file.txt")
        self.assertEqual(
            result,
            'Error: File not found or is not a regular file: "non_existent_file.txt"',
        )
        print(result)

    def test_get_file_content_is_directory(self):
        result = get_file_content(".", "pkg")
        self.assertEqual(
            result, 'Error: File not found or is not a regular file: "pkg"'
        )
        print(result)

    def test_get_file_content_outside_dir(self):
        result = get_file_content("calculator", "../any_file.py")
        self.assertEqual(
            result,
            'Error: Cannot read "../any_file.py" as it is outside the permitted working directory',
        )
        print(result)

    def test_get_file_content_absolute_path(self):
        result = get_file_content(".", "/etc/passwd")
        self.assertEqual(
            result,
            'Error: Cannot read "/etc/passwd" as it is outside the permitted working directory',
        )
        print(result)


if __name__ == "__main__":
    unittest.main()
