from telemetry.protocol import parse_frame

class FrameDecoder:
    def __init__(self):
        self.buffer = bytearray()

    def feed(self, chunk: bytes):
        self.buffer.extend(chunk)
        results = []
        while len(self.buffer) >= 4:
            candidate = bytes(self.buffer[:4])
            value = parse_frame(candidate)
            if value is not None:
                results.append(value)
                del self.buffer[:4]
            else:
                del self.buffer[:1]
        # We’ll decode complete messages here.

        return results