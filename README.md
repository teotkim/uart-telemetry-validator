# MSPM0 UART telemetry analyzer — first milestone

This is a learning project based on the four-byte UART message described in Teo's ECE 319K Lab 8 handout. The handout specifies 2,000 bit/s and a nominal 30 Hz sample rate. Each message has a start byte `<` followed by three ASCII digits. For example, `<154` represents 1.54 cm; the original 1.547 cm sample is truncated to hundredths. Four 10-bit UART frames occupy about 20 ms on the wire. These are protocol specifications, not results from this Python program.

## Your task: implement the parser

Open `telemetry/protocol.py` and fill in `parse_frame` yourself. It must:

1. Reject any input that is not exactly four bytes long.
2. Reject a message that does not begin with `<`.
3. Reject a message containing a nondigit after `<`.
4. Return distance in centimeters as a `float` when valid. For `<154`, return `1.54`.

Keep the implementation straightforward. `frame[1:]` selects the three digits; `bytes.isdigit()` checks them; `int(...) / 100` converts to centimeters.

Run the tests in a terminal from this directory:

```bash
python3 -m unittest discover -s tests -v
```

The tests intentionally fail until you implement the function. Then change a test input or add your own case and rerun the suite.

## Git practice (after your code passes)

```bash
git init
git status
git add README.md telemetry tests .gitignore
git commit -m "Parse four-byte MSPM0 telemetry frames"
git log --oneline
```

You can complete this project without the old hardware. Label generated input as synthetic and describe the result as a protocol parser/test harness, not a live UART capture or an improvement to your original board setup. A terminal session on macOS is good Python/Git practice; the resume's *Linux* claim requires you to repeat the workflow on Linux, such as Ubuntu or WSL.

## Next milestones

- Streaming decoder: accept arbitrarily split and malformed byte chunks and resynchronize on `<`.
- Synthetic replay: generate byte streams and timestamped examples with delayed, missing, and corrupted messages; label the fixtures as simulated.
- Analysis: plot decoded values from the synthetic replay and flag long inter-message intervals as *possible* missed samples. The protocol has no sequence counter, so a gap cannot prove precisely which samples were lost.
- Optional hardware extension only if you later have access to a board and USB-to-UART adapter: capture real output with the correct voltage, common ground, and serial settings.
- FreeRTOS: if you still have an MSPM0G3507 board, start from TI's `empty_freertos` example, then build a small ADC/UART producer-consumer exercise. If you do not, we can use a supported simulator and word the resume accordingly. Only claim a game refactor if the game itself is actually ported and tested.
