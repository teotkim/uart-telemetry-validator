import unittest

from telemetry.protocol import parse_frame


class ParseFrameTests(unittest.TestCase):
    def test_valid_sample(self):
        self.assertEqual(parse_frame(b"<154"), 1.54)

    def test_zero(self):
        self.assertEqual(parse_frame(b"<000"), 0.0)

    def test_wrong_start(self):
        self.assertIsNone(parse_frame(b">154"))

    def test_nondigit(self):
        self.assertIsNone(parse_frame(b"<1X4"))

    def test_incomplete(self):
        self.assertIsNone(parse_frame(b"<15"))

    def test_extra_byte(self):
        self.assertIsNone(parse_frame(b"<1547"))


if __name__ == "__main__":
    unittest.main()
