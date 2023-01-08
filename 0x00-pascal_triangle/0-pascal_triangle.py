#!/usr/bin/python3
"""pascal triangle implementation with python"""


def pascal_triangle(n):
    """pascal triangle"""
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]

    mainlist = [[1], [1, 1]]
    for i in range(1, n - 1):
        list1 = [1]
        for j in range(len(mainlist[i]) - 1):
            list1.append(mainlist[i][j] + mainlist[i][j + 1])
        list1.append(1)
        mainlist.append(list1)
    return mainlist
