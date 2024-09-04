#!/usr/bin/python3
def validUTF8(data):
    num_bytes = 0

    for num in data:
        # Get the binary representation of the number, without the '0b' prefix, and zero-padded to 8 bits
        bin_rep = format(num, '#010b')[-8:]

        if num_bytes == 0:
            # Determine how many bytes are in this UTF-8 character
            if bin_rep[0] == '0':
                continue  # 1-byte character
            elif bin_rep[:3] == '110':
                num_bytes = 1  # 2-byte character
            elif bin_rep[:4] == '1110':
                num_bytes = 2  # 3-byte character
            elif bin_rep[:5] == '11110':
                num_bytes = 3  # 4-byte character
            else:
                return False  # Invalid UTF-8 header
        else:
            # If we are expecting more bytes, they must be of the form 10xxxxxx
            if bin_rep[:2] != '10':
                return False
            num_bytes -= 1

    return num_bytes == 0
