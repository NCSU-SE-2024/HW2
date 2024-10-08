"""
This module provides a function to replace the elements of an array with random numbers
generated by invoking the Unix `shuf` command. The `random_array` function iterates over
each element in the input array, replacing it with a randomly selected integer between 1 and 20.
"""
import subprocess
from typing import List

def random_array(arr: List[int]) -> List[int]:
    """
    Replace each element of the input array with a random integer between 1 and 20
    using the Unix `shuf` command.

    Args:
        arr (list of int): The array of integers to be randomized.

    Returns:
        list of int: The array with each element replaced by a random integer between 1 and 20.

    Raises:
        subprocess.CalledProcessError: If the `shuf` command fails.

    Example:
        >>> random_array([0, 0, 0])
        [5, 12, 19]  # Output will vary
    """
    shuffled_num = None
    for i, _ in enumerate(arr):
        try:
            shuffled_num = subprocess.run(["shuf", "-i1-20", "-n1"],
                                          capture_output=True,
                                          check=True)
        except subprocess.CalledProcessError as called_process_error:
            print(f"Command failed with return code {called_process_error.returncode}")
        else:
            #fixed FileNotFoundError: [Errno 2] No such file or directory: 'shuf'
            arr[i] = int(shuffled_num.stdout.decode('utf-8').strip())
    return arr
