#!/usr/bin/python3
""" Script for parsing log data from stdin and computing metrics. """

import sys
import signal

# Initialize counters and total file size.
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
total_size = 0
line_count = 0

def print_stats():
    """ Prints accumulated statistics from log data. """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def handle_signal(sig, frame):
    """ Handles SIGINT (e.g., CTRL+C) by printing stats and exiting. """
    print_stats()
    sys.exit(0)

# Register signal handler for handling CTRL+C.
signal.signal(signal.SIGINT, handle_signal)

try:
    # Read from stdin line by line.
    for line in sys.stdin:
        parts = line.strip().split()
        if len(parts) < 7 or not parts[-2].isdigit():
            continue  # Skip invalid format lines.

        file_size = int(parts[-1])
        status_code = parts[-2]

        total_size += file_size

        if status_code in status_codes:
            status_codes[status_code] += 1

        line_count += 1

        if line_count == 10:
            print_stats()
            line_count = 0

except KeyboardInterrupt:
    # Print stats in case of program interruption.
    print_stats()

finally:
    # Ensure final stats are printed when stream ends.
    print_stats()
