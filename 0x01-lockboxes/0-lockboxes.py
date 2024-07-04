#!/usr/bin/python3
"""
Module 0-lockboxes
Contains function that determines if all boxes can be opened
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened

    Parameters:
    boxes (list of list of int): list of boxes with keys

    Returns:
    bool: True if all boxes can be opened, False otherwise
    """
    if not boxes:
        return False

    unlocked = set()
    keys = [0]  # Start with the first box unlocked

    while keys:
        key = keys.pop()
        if key not in unlocked:
            unlocked.add(key)
            for new_key in boxes[key]:
                if new_key not in unlocked:
                    keys.append(new_key)

    return len(unlocked) == len(boxes)
