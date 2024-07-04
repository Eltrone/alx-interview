#!/usr/bin/python3
def canUnlockAll(boxes):
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

# Test cases
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # False
