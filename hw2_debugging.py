"""
This module performs a merge sort on an array that is randomly populated using a shell command.
"""

import logging
import rand

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def merge_sort(input_arr):
    """
    Sorts an array using the merge sort algorithm.

    Args:
        arr (list): The list of elements to be sorted.

    Returns:
        list: The sorted list.
    """
    logger.info(input_arr)
    if len(input_arr) == 1:
        return input_arr

    half = len(input_arr) // 2
    logger.info(half)

    return recombine(merge_sort(input_arr[:half]), merge_sort(input_arr[half:]))


def recombine(left_arr, right_arr):
    """
    Merges two sorted arrays into one sorted array.

    Args:
        left_arr (list): The left half of the array.
        right_arr (list): The right half of the array.

    Returns:
        list: The merged and sorted array.
    """
    left_index = 0
    right_index = 0
    print("left Arr: ", left_arr)
    print("right Arr: ", right_arr)
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1

    if right_index < len(right_arr):
        for i in range(right_index, len(right_arr)):
            merge_arr[left_index + i] = right_arr[i]

    if left_index < len(left_arr):
        for i in range(left_index, len(left_arr)):
            merge_arr[i + right_index] = left_arr[i]

    print("Merge Arr: ", merge_arr)
    return merge_arr

arr = rand.random_array([None]*20)
logger.info(arr)
arr_out = merge_sort(arr)

print(arr_out)