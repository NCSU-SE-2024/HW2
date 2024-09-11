"""
This modules provides an implementation of the merge and selection sort algorithm.
"""
import hw2_debugging
import debugging


def test1():
    """
    Test Case 1: Standard Case (Mixed Integers)
    This test case checks if the function can sort a typical unsorted array of integers.
    """
    input_arr = [23, 10, 5, 8, 1, 2, 3, 9, 11]
    output_arr = [1, 2, 3, 5, 8, 9, 10, 11, 23]
    assert hw2_debugging.merge_sort(
        input_arr) == output_arr, "Testcase 1 Failed"


def test2():
    """
    Test Case 2: Edge Case (Empty Array)
    This test case checks if the function can handle an empty array.
    """
    input_arr = []
    output_arr = []
    assert hw2_debugging.merge_sort(
        input_arr) == output_arr, "Testcase 2 Failed" # type: ignore
    #ignore above warning as we want to test for empty array


def test3():
    """
    Test Case 3: Standard Case (Array with Duplicates and Negative Integers)
    This test case checks if the function can handle an duplicates and negative integers.
    """
    input_arr = [5, 2, 9, -1, 5, 6, 2, -9, 5]
    output_arr = [-9, -1, 2, 2, 5, 5, 5, 6, 9]
    assert hw2_debugging.merge_sort(
        input_arr) == output_arr, "Testcase 3 Failed"

def test4():
    """
    Test Case 4: Standard Case (Mixed Integers)
    This test case checks if the function can sort a typical unsorted array of integers.
    """
    input_arr = [23, 10, 5, 8, 1, 2, 3, 9, 11]
    output_arr = [1, 2, 3, 5, 8, 9, 10, 11, 23]
    assert debugging.selection_sort(
        input_arr) == output_arr, "Testcase 4 Failed"


def test5():
    """
    Test Case 5: Edge Case (Empty Array)
    This test case checks if the function can handle an empty array.
    """
    input_arr = []
    output_arr = []
    assert debugging.selection_sort(
        input_arr) == output_arr, "Testcase 2 Failed" # type: ignore
    #ignore above warning as we want to test for empty array


def test6():
    """
    Test Case 6: Standard Case (Array with Duplicates and Negative Integers)
    This test case checks if the function can handle an duplicates and negative integers.
    """
    input_arr = [5, 2, 9, -1, 5, 6, 2, -9, 5]
    output_arr = [-9, -1, 2, 2, 5, 5, 5, 6, 9]
    assert debugging.selection_sort(
        input_arr) == output_arr, "Testcase 3 Failed"
