import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

from textutil import slugify, truncate


class TextUtilTests(unittest.TestCase):
    def test_slugify_basic(self):
        self.assertEqual(slugify("Hello World"), "hello-world")

    def test_truncate_short_text_untouched(self):
        self.assertEqual(truncate("abcdef", 10), "abcdef")


if __name__ == "__main__":
    unittest.main()
