#!/usr/bin/python3
"""
defines the function minOperations
"""
from math import sqrt


def minOperations(n):
    """
       calculates the fewest number of operations needed
       to result in exactly n H characters in the file
    """

    if sqrt(n) == int(sqrt(n)):
        return (int(sqrt(n)) * 2)

    n_list = []
    for i in range(1, n):
        if n % i == 0 and i != 1:
            n_list.append(i)
    len_n_list = len(n_list)
    if len_n_list != 0:
        if len_n_list == 2:
            return n_list[0] * 2
        min_odd = min([x for x in n_list if x & 1])
        if min_odd:
            return len_n_list + min_odd
        else:
            return len_n_list * 2
    return 0
