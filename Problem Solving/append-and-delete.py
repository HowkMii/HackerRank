#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    c=0
    for i,j in zip(s,t):
        if i== j:
            c+=1
        else:
            break

    t_len=len(s)+len(t)
    if t_len <= 2*c + k and t_len%2 == k%2 or t_len<k:
        return"Yes"
    else:
        return"No"




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
