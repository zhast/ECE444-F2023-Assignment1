import unittest
from utils import Utils


# Credit to ChatGPT

class TestUtils(unittest.TestCase):
    def test_reverse_integer(self):
        self.assertEqual(Utils.reverse_number(12345), 54321)
        self.assertEqual(Utils.reverse_number(0), 0)
        self.assertEqual(Utils.reverse_number(-6789), -9876)

    def test_reverse_invalid_input(self):
        with self.assertRaises(ValueError):
            Utils.reverse_number("123")
        with self.assertRaises(ValueError):
            Utils.reverse_number(123.45)

    def test_format_integer(self):
        binary, octal = Utils.format_number(42)
        self.assertEqual(binary, '0b101010')
        self.assertEqual(octal, '0o52')

    def test_format_invalid_input(self):
        with self.assertRaises(ValueError):
            Utils.format_number("42")
        with self.assertRaises(ValueError):
            Utils.format_number(42.0)


if __name__ == '__main__':
    unittest.main()
