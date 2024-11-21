#!/usr/bin/python3
'''Minimum Operations'''


def minOperations(n):
    # calculates the fewest number

    p_char = 1
    clipboard = 0
    i = 0

    while p_char < n:
        if clipboard == 0:
            clipboard = p_char
            i += 1

        if p_char == 1:
            p_char += clipboard
            i += 1
            continue

        remaining = n - p_char

        if remaining < clipboard:
            return 0

        if remaining % p_char != 0:
            p_char += clipboard
            i += 1
        else:
            clipboard = p_char
            p_char += clipboard
            i += 2

    if p_char == n:
        return i
    else:
        return 0
