#!/usr/bin/python3
import sys
import signal

def signal_handler(sig, frame):
    """ Handle SIGINT to print stats on keyboard interruption """
    print_stats()
    sys.exit(0)

def print_stats():
    """ Print the current log parsing statistics """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

# Initialize status codes and total file size
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_size = 0
line_count = 0

# Setup signal handling for keyboard interruption (CTRL+C)
signal.signal(signal.SIGINT, signal_handler)

try:
    # Read from stdin line by line
    for line in sys.stdin:
        parts = line.strip().split()
        if len(parts) != 12 or not parts[5].isdigit() or not parts[6].isdigit():
            continue  # Skip the line if format is incorrect

        status_code = int(parts[5])
        file_size = int(parts[6])

        # Update the status code count and total file size
        if status_code in status_codes:
            status_codes[status_code] += 1
            total_size += file_size
            line_count += 1

        # Print statistics every 10 lines or on keyboard interruption
        if line_count == 10:
            print_stats()
            line_count = 0

except KeyboardInterrupt:
    # Ensure stats are printed even if program is interrupted
    print_stats()
