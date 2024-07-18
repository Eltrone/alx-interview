#!/usr/bin/python3
import sys
import signal

def signal_handler(sig, frame):
    """Handle the SIGINT signal and print current statistics before exiting."""
    print_stats()
    sys.exit(0)

def print_stats():
    """Print the cumulative statistics of the logs."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

# Initialize variables
status_codes = {200:0, 301:0, 400:0, 401:0, 403:0, 404:0, 405:0, 500:0}
total_size = 0
line_count = 0

# Set up signal handling for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) != 7 or parts[3] != '"GET':
            continue  # Skip the line if it does not match the expected format
        try:
            status_code = int(parts[5])
            file_size = int(parts[6])
        except ValueError:
            continue  # Skip the line if status code or file size are not integers

        if status_code in status_codes:
            status_codes[status_code] += 1
            total_size += file_size
            line_count += 1

        if line_count == 10:
            print_stats()
            line_count = 0

except KeyboardInterrupt:
    print_stats()  # Ensure stats are printed on CTRL+C as well
