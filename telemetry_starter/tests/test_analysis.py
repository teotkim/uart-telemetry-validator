import unittest
from telemetry.analysis import find_long_gaps


class GapTests(unittest.TestCase):
    def test_flags_long_gap(self):
        self.assertEqual(find_long_gaps([0, 33, 99]), [99])

    def test_no_long_gap(self):
        self.assertEqual(find_long_gaps([0, 33, 66]), [])