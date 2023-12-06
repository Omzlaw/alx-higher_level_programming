#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # If the mid element is greater than its right neighbor, a peak may be to the left
            high = mid
        else:
            # If the mid element is less than or equal to its right neighbor, a peak may be to the right
            low = mid + 1

    return list_of_integers[low]
