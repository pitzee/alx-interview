#!/usr/bin/python3
# python3 header


def canUnlockAll(boxes):
    # This function checks if all boxes can be unlocked.

    opened = [False] * len(boxes)
    opened[0] = True
    stack = [key for key in boxes[0]]
    while stack:
        key = stack.pop()
        if not opened[key]:
            opened[key] = True
            for new_key in boxes[key]:
                if new_key < len(boxes) and not opened[new_key]:
                    stack.append(new_key)
    return all(opened)
