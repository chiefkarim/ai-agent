import os
import unittest
import tempfile
import shutil

from functions.utils import check_dir_within_working_dir_boundry
from functions.write_file import write_file


class TestWriteFile(unittest.TestCase):
    root_tmp_dir = tempfile.gettempdir() + "/hello"

    def tearDown(self) -> None:
        if os.path.isdir(self.root_tmp_dir):
            shutil.rmtree(self.root_tmp_dir)

    def test_file_outside_working_dir(self):
        working_dir = "./calculator/"
        target_file = "../hello.txt"

        result = write_file(working_dir, target_file, "hello world")

        print("test-result: ", result)
        self.assertIn(
            f'Error: Cannot write to "{target_file}" as it is outside the permitted working directory',
            result,
        )

    def test_directory_should_throw_error(self):
        working_dir = "./calculator/"
        target_file = "pkg/"

        result = write_file(working_dir, target_file, "hello world")
        print("test-result: ", result)

        self.assertEqual(
            f'Error: Cannot write to "{target_file}" as it is a directory', result
        )

    def test_should_creat_sub_dirs_that_dont_exist(self):
        working_dir = self.root_tmp_dir
        target_file = "./hello/another/hello.txt"
        target_file_valid, _ = check_dir_within_working_dir_boundry(
            working_dir, target_file
        )
        last_sub_dir = target_file_valid.split("/")
        last_sub_dir.pop()
        last_sub_dir = "/".join(last_sub_dir)

        result = write_file(working_dir, target_file, "hello world")

        self.assertNotIn("Error:", result)
        self.assertTrue(os.path.isdir(last_sub_dir))

    def test_should_write_content_to_file(self):
        working_dir = self.root_tmp_dir
        target_file = "./hello/another/hello.txt"
        target_file_valid, _ = check_dir_within_working_dir_boundry(
            working_dir, target_file
        )
        content = "hello world"

        result = write_file(working_dir, target_file, content)

        self.assertTrue(os.path.isfile(target_file_valid))
        with open(target_file_valid, "r") as f:
            self.assertEqual("hello world", f.read(11))
        self.assertNotIn("Error:", result)
        self.assertEqual(
            result,
            f'Successfully wrote to "{target_file}" ({len(content)} characters written)',
        )


if __name__ == "__main__":
    unittest.main()
