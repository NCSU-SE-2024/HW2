"""
This module provides an implementation of the selection sort algorithm.
"""


def selection_sort(arr):
    """
    Sorts an array in ascending order using the selection sort algorithm.

    Args:
        input_array (list): The list of elements to be sorted.

    Returns:
        list: The sorted list.
    """
    length_arr = len(arr)
    for i in range(length_arr):
        lowest_index = i
        for j in range(length_arr):
            if arr[j] < arr[lowest_index]:
                lowest_index = j

        arr[lowest_index] = arr[i]
        arr[i] = arr[lowest_index]
        length_arr = length_arr - 1

    return arr


arr_in = [5, 3, 2, 1, 8, 10, 11, 9, 23]

arr_out = selection_sort(arr_in)

print(arr_out)
