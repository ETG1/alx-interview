#!/usr/bin/python3
"""Script that reads each line of input from stdin and computes various metrics
"""

import sys


def process_logs():
    cache = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }
    total_size = 0
    counter = 0

    try:
        for line in sys.stdin:
            line_list = line.split(" ")
            if len(line_list) > 4:
                code = line_list[-2]
                size = int(line_list[-1])
                if code in cache.keys():
                    cache[code] += 1
                total_size += size
                counter += 1

            if counter == 10:
                counter = 0
                print_stats(total_size, cache)

    except Exception as err:
        pass

    finally:
        print_stats(total_size, cache)


def print_stats(file_size_total, status_code_counts):
    print('File size: {}'.format(file_size_total))
    for key, value in sorted(status_code_counts.items()):
        if value != 0:
            print('{}: {}'.format(key, value))


if __name__ == "__main__":
    process_logs()
