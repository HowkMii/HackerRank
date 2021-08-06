#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    if n == 1:
        return n
    else:
        return n * extraLongFactorials(n - 1)

if __name__ == '__main__':
    n = int(input().strip())

    a=extraLongFactorials(n)
    print(a)
