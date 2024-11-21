#!/usr/bin/python3
'''LockBoxes'''


def canUnlockAll(boxes):
    '''Determines if all the boxes can be opened.

    Args:
        boxes (list of list of int): Each box contains a list of keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    '''

    num_boxes = len(boxes)
    opened_boxes = set([0])
    keys_collected = boxes[0]

    while keys_collected:
        current_key = keys_collected.pop(0)
        if current_key < num_boxes and current_key not in opened_boxes:
            opened_boxes.add(current_key)
            keys_collected.extend(boxes[current_key])

            if len(opened_boxes) == num_boxes:
                return True

    return len(opened_boxes) == num_boxes#!/usr/bin/python3
