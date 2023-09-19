#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr_max, arr_min = arr.copy(), arr.copy()
    _ = arr_max.remove(min(arr_max))
    _ = arr_min.remove(max(arr_min))

    max_val = sum(arr_max)
    min_val = sum(arr_min)

    print(f"{min_val} {max_val}")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
