#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr):
    # Write your code here
    n = len(arr)
    d %= n  # Ensure d is within the array length
    # Rotate by slicing
    # print(d)
    rotated_array = arr[d:] + arr[:d]
    print(arr[d:])
    print(arr[:d])
    return rotated_array
if __name__ == '__main__':


    n = 5

    d = 3

    arr = [1,2,3,4,5]

    result = rotateLeft(d, arr)

    print(result)
