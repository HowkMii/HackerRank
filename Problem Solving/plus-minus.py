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
    p = ng = z =0
    for i in range(n):
        if arr[i]>0:
            p +=1
        elif arr[i]<0:
            ng +=1
        else:
            z +=1
    print(p/n)
    print(ng/n)
    print(z/n)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
