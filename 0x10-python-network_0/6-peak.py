#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """Finds the peak of a list"""
    if list_of_integers:
        return max(list_of_integers)
