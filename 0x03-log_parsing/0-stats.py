#!/usr/bin/python3
""" Script to parse log data from stdin and compute metrics. """

import sys
import signal
import re

# Initialize counters and total file size.
status_codes = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
}
total_file_size = 0
line_count = 0


def print_stats():
    """ Prints accumulated statistics from log data. """
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def handle_signal(sig, frame):
    """ Handles SIGINT (CTRL+C) by printing stats and exiting. """
    print_stats()
    sys.exit(0)


# Register signal handler for handling CTRL+C.
signal.signal(signal.SIGINT, handle_signal)

# Regex pattern to match the required log format
log_pattern = re.compile(
    r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] '
    r'"GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'
)


try:
    # Read from stdin line by line.
    for line in sys.stdin:
        match = log_pattern.match(line.strip())
        if match:
            ip, date, status_code, file_size = match.groups()
            file_size = int(file_size)
            status_code = status_code

            total_file_size += file_size

            if status_code in status_codes:
                status_codes[status_code] += 1

            line_count += 1

            if line_count == 10:
                print_stats()
                line_count = 0

except KeyboardInterrupt:
    print_stats()

finally:
    print_stats()
