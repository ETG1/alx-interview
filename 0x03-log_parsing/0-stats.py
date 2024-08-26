#!/usr/bin/python3

import sys
import re
import signal

# Define regex pattern to match log lines
LOG_PATTERN = re.compile(
    r'^(?P<ip>\S+) - \[(?P<date>[^\]]+)\] "(?P<method>[A-Z]+) (?P<url>\S+) HTTP/\d\.\d" (?P<status>\d{3}) (?P<size>\d+)$'
)

# Initialize dictionaries and counters
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_file_size = 0
line_count = 0

def print_statistics():
    global status_counts, total_file_size
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_counts):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")

def signal_handler(signum, frame):
    print_statistics()
    sys.exit(0)

def main():
    global total_file_size, line_count

    # Set up signal handling for keyboard interruption
    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            line_count += 1
            match = LOG_PATTERN.match(line)
            if match:
                status_code = int(match.group('status'))
                file_size = int(match.group('size'))
                if status_code in status_counts:
                    status_counts[status_code] += 1
                    total_file_size += file_size

            if line_count % 10 == 0:
                print_statistics()

    except KeyboardInterrupt:
        print_statistics()
        sys.exit(0)

if __name__ == "__main__":
    main()

