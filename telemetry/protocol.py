"""Decode a single complete UART telemetry message."""
from typing import Optional

def parse_frame(frame: bytes) -> Optional[float]:
    """Return distance in centimeters, or None for an invalid frame.

    The four bytes are b'<' followed by three ASCII digits. The last digit
    represents hundredths of a centimeter, so b'<154' means 1.54 cm.
    """
    # TODO: implement the four checks/conversion described in README.md.
    if len(frame) != 4:
        return None
    if frame[:1] != b"<":
        return None
    if not frame[1:].isdigit():
        return None
    return int(frame[1:]) / 100