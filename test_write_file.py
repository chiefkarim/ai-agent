import unittest

from functions.write_file import write_file


class TestWriteFile(unittest.TestCase):
    def test_nothing(self):
        result = write_file(".", ".", "hello world")
        print("test-result: ", result)
