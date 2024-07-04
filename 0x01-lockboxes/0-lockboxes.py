#!/usr/bin/python3
"""
Module that defines the canUnlockAll function.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
    boxes (list of list of int):list where each sublist represents the keys
                                     contained in a specific box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    unlocked_boxes = set()
    keys = [0]
    unlocked_boxes.add(0)

    while keys:
        current_key = keys.pop(0)
        for key in boxes[current_key]:
            if key < len(boxes) and key not in unlocked_boxes:
                unlocked_boxes.add(key)
                keys.append(key)

    return len(unlocked_boxes) == len(boxes)
