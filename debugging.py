"""
This module sets up logging for debugging purposes and writes a test log entry.

The logging configuration is set to write log messages to a file named 'partial_debugging.log'.
Log messages are encoded in UTF-8 and formatted to include the timestamp and the log message.
The logging level is set to DEBUG, meaning that all messages of level DEBUG and higher will
be recorded.

Usage:
    Run this script to initialize logging settings and create a log entry with a DEBUG level
    message.
"""
import logging
from typing import List

logging.basicConfig(
    filename='partial_debugging_selection_sort.log',
    encoding='utf-8',
    level=logging.DEBUG,
    format='%(asctime)s %(message)s')
logging.debug("NEW LOG")


def selection_sort(arr: List[int]) -> List[int]:
    """
    Sorts an array in ascending order using the selection sort algorithm.

    Args:
        input_array (list): The list of elements to be sorted.

    Returns:
        list: The sorted list.
    """
    logger = logging.getLogger(__name__)
    length_arr = len(arr)
    for i in range(length_arr):
        lowest_index = i
        # changed range of j from "0 - len_arr" to "i+1 - len_arr"
        for j in range(i + 1, length_arr):
            # what index contains the lowest value?
            logger.debug("lowest index: %r", lowest_index)
            if arr[j] < arr[lowest_index]:
                lowest_index = j

        # where in the array should the ith smallest value be?
        logger.debug("i: %r", i)
        # where are we considering the end of the array?
        logger.debug("length_arr: %r", length_arr)

        # lowest_num = arr[lowest_index]
        # logger.debug("lowest_num: %r",lowest_num) # lowest number found in
        # unsorted array

        # logger.debug("before: %r", arr) # array state before we swap anything
        # arr[lowest_index] = arr[i]
        # logger.debug("first: %r", arr) # array state after the first change
        # arr[i] = lowest_num
        # logger.debug("final: %r", arr) # array state after the second change
        # length_arr = length_arr - 1

        # changed implementation way of swapping elements i.e. without temp
        # var"
        arr[i], arr[lowest_index] = arr[lowest_index], arr[i]

    return arr


arr_in = [5, 3, 2, 1, 8, 10, 11, 9, 23]

arr_out = selection_sort(arr_in)

print(arr_out)
