def canUnlockAll(boxes):
    '''
    Determines if all boxes can be opened.
    Parameters:
    boxes (list of lists): A list where each element is a list containing keys to other boxes.
    Returns:
    bool: True if all boxes can be opened, False otherwise.
    '''

    n = len(boxes)  
    opened_boxes = set([0])
    keys = set(boxes[0])

    while keys:
        new_keys = set()
        for key in keys:
            if key < n and key not in opened_boxes:
                opened_boxes.add(key)
                new_keys.update(boxes[key])

        keys = new_keys

        if len(opened_boxes) == n:
            return True

    return len(opened_boxes) == n

