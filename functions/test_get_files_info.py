import unittest
from get_files_info import get_files_info


class TestGetFilesInfo(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_calculator_directory(self):
        result = get_files_info("calculator", ".")

        self.assertIn("Result for current directory:", result)
        self.assertRegex(result, r"- main\.py: file_size=\d+ bytes, is_dir=False")
        self.assertRegex(result, r"- tests\.py: file_size=\d+ bytes, is_dir=False")
        self.assertRegex(result, r"- pkg: file_size=\d+ bytes, is_dir=True")

    def test_calculator_pkg(self):
        result = str.split(get_files_info("calculator", "pkg"), "\n")

        self.assertTrue(3 <= len(result))
        self.assertIn("Result for current directory:", result[0])
        joined_res = str.join("\n", result)
        self.assertRegex(
            joined_res,
            r"- calculator.py: file_size=\d+ bytes, is_dir=False",
        )
        self.assertRegex(joined_res, r"- render.py: file_size=\d+ bytes, is_dir=False")


if __name__ == "__main__":
    unittest.main()
