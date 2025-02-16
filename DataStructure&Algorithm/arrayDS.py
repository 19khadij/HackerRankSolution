#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def reverseArray(a):
    # Write your code here
    left=0
    right= len(a)-1

    while left<right:
        print(left,right)
        a[left],a[right]=a[right],a[left]
        
        left+=1
        right-=1

    return a
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # arr_count = int(input().strip())

    arr = [1,4,3,2]

    res = reverseArray(arr)
    print(res)
    # fptr.write(' '.join(map(str, res)))
    # fptr.write('\n')

    # fptr.close()
