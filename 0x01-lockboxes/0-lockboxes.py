#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened or not.

    Args:
        boxes (list of lists): List of boxes, where each box is a list of keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    # Keep track of the boxes that have been opened
    opened_boxes = {0}  # The first box is already opened by default

    # Use a set to keep track of keys to be checked
    keys_to_check = set(boxes[0])

    # Process keys in the set until it's empty
    while keys_to_check:
        key = keys_to_check.pop()
        if key not in opened_boxes:
            opened_boxes.add(key)
            keys_to_check.update(boxes[key])

    # Check if all boxes have been opened
    return len(opened_boxes) == len(boxes)
