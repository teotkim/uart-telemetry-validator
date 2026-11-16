def find_long_gaps(times_ms, threshold_ms=50):
    flagged = []

    for index in range(1, len(times_ms)):
        previous_time = times_ms[index - 1]
        current_time = times_ms[index]
        gap_ms = current_time - previous_time

        if gap_ms > threshold_ms:
            flagged.append(current_time)

    return flagged