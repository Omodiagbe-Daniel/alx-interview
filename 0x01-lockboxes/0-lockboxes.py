#!/usr/bin/python3
"""Lockboxes project: it determines if a box can be opened"""


def canUnlockAll(boxes):
    """You have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1 and
    each box may contain keys to the other boxes"""

    opened_boxes = [0]
    size = len(boxes)
    for id in range(size):
        for box in (boxes):
            if box == []:
                break
            for ele in box:
                if ele < size and ele != id and ele not in opened_boxes:
                    opened_boxes.append(ele)

    if len(opened_boxes) == size:
        return True
    else:
        return False
