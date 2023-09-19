#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    n = len(arr)
    pos_elements = len([a for a in arr if a > 0])
    neg_elements = len([a for a in arr if a < 0])
    zero_elements = len([a for a in arr if a == 0])
    print("{:.6f}".format(pos_elements/n))
    print("{:.6f}".format(neg_elements/n))
    print("{:.6f}".format(zero_elements/n))

# Another Solution
def plusMinus(arr):
    # Write your code here
    n = len(arr)
    pos_elements, neg_elements, zero_elements = 0, 0, 0
    for a in arr:
        if a > 0:
            pos_elements +=1
        elif a == 0:
            zero_elements +=1
        else: 
            neg_elements +=1
            
    print("{:.6f}".format(pos_elements/n))
    print("{:.6f}".format(neg_elements/n))
    print("{:.6f}".format(zero_elements/n))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
