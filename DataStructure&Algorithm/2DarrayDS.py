#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    # print(arr)
    # print(arr[0][0],arr[0][1],arr[0][2])
    # print('',arr[0][1],'')
    # print(arr[0][0],arr[0][1],arr[0][2])
    
    rows=len(arr)
    col=len(arr[0])
    mini=float('-inf')
    for i in range(rows -2):
        for j in range(col-2):
            sums=arr[i][j]+arr[i][j+1]+arr[i][j+2] +arr[i+1][j+1] +arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]

            
            mini=max(mini,sums)
    return mini

if __name__ == '__main__':
    
    arr = [[[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]]

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    print(result)