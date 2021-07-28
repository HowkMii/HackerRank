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
    s=0
    minn=9999999
    maxx=0
    n=len(arr)
    for i in range(n):
        s +=arr[i]
        minn=min(minn,arr[i])
        maxx=max(maxx,arr[i])
    print(s-maxx,s-minn)
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
