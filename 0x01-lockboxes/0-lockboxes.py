#!/usr/bin/python3
# python3 header


def canUnlockAll(boxes):
    # This function checks if all boxes can be unlocked.
    number_of_boxes = len(boxes)
    unlocked_boxes = [False] * number_of_boxes
    unlocked_boxes[0] = True
    keys = [key for key in boxes[0]]

    for key in keys:
        if not unlocked_boxes[key]:
            unlocked_boxes[key] = True
            keys += boxes[key]

    return all(unlocked_boxes)
