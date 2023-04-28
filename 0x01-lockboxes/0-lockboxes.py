#!/usr/bin/python3
"""lockbox challenge"""


def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened."""
    open_boxes = len(boxes)
    unlocked_boxes = set([0])   # starts with the first box unlocked
    keys_to_check = set(boxes[0])   # collects keys from the first box
    while keys_to_check:
        key = keys_to_check.pop()
        if key < open_boxes and key not in unlocked_boxes:
            unlocked_boxes.add(key)
            keys_to_check.update(boxes[key])
    return len(unlocked_boxes) == open_boxes
