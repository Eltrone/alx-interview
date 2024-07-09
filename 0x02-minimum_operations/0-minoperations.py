#!/usr/bin/python3
"""
Defines a function that calculates the minimum number of operations
needed to achieve exactly n H characters in the file using
Copy All and Paste operations.
"""


def minOperations(n):
    """
    Calculate minimum number of operations to get `n` char by Copy All & Paste

    Args:
        n (int): the target number of characters

    Returns:
        int: minimum number of operation required, or 0 if `n` cant be reached
    """
    if n <= 1:
        return 0
    operations = 0
    current_factor = 2
    while n > 1:
        while n % current_factor == 0:
            operations += current_factor
            n /= current_factor
        current_factor += 1
    return operations

# You can test the function with:
# n = 4
# print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
# n = 12
# print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
