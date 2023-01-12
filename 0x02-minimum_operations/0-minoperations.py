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

    if n > 0:
        if sqrt(n) == int(sqrt(n)):
            if (sqrt(n)) % 2 != 0:
                return (int(sqrt(n)) * 2)
        if sqrt(n) % 2 == 0:
            return int(sqrt(n)) + 2
        n_list = []
        for i in range(1, n):
            if n % i == 0 and i != 1:
                n_list.append(i)
        len_n_list = len(n_list)
        if len_n_list == 0:
            return n
        if len_n_list == 2:
            return n_list[0] * 2
        odd_list = []

        for odd in n_list:
            if odd & 1:
                odd_list.append(odd)
        if odd_list != []:
            return len_n_list + min(odd_list)
        else:
            return (len_n_list + 1) * 2
    return 0
