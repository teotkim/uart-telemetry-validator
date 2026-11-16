from telemetry.stream import FrameDecoder
from telemetry.analysis import find_long_gaps
import matplotlib.pyplot as plt

samples = [
    (0, b"<154"),
    (33, b"<155"),
    (99, b"<157"),
]

distances_cm = []
decoder = FrameDecoder()
for time_ms, frame in samples:
    readings = decoder.feed(frame)
    print(time_ms, readings)
    distances_cm.extend(readings)

times_ms = [sample[0] for sample in samples]

for time_ms in find_long_gaps(times_ms):
    print(f"Possible missed sample before {time_ms} ms")

fig, ax = plt.subplots()
ax.scatter(times_ms, distances_cm)

for gap_time in find_long_gaps(times_ms):
    ax.axvline(gap_time, color="crimson", linestyle="--",
               label="Long interval before reading")
ax.legend()

ax.set(
    xlabel="Time (ms)",
    ylabel="Distance (cm)",
    title="Synthetic UART telemetry",
)
fig.savefig("synthetic_telemetry_scatter.png", dpi=150)
plt.close(fig)