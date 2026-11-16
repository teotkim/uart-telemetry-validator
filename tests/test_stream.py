import unittest
from telemetry.stream import FrameDecoder


class FrameDecoderTests(unittest.TestCase):
    def test_recovers_after_bad_bytes(self):
        decoder = FrameDecoder()
        self.assertEqual(decoder.feed(b"x<2A0<235"), [2.35])
    def test_split_frame(self):
        decoder = FrameDecoder()
        self.assertEqual(decoder.feed(b"<1"), [])
        self.assertEqual(decoder.feed(b"54"), [1.54])
        self.assertEqual(decoder.feed(b"x<2A0<235"), [2.35])