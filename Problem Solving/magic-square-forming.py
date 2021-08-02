import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
M =[[[8, 3, 4],[1, 5, 9],[6, 7, 2]],
    [[6, 1, 8],[7, 5, 3],[2, 9, 4]],
    [[2, 7, 6],[9, 5, 1],[4, 3, 8]],
    [[4, 9, 2],[3, 5, 7],[8, 1, 6]],
    [[4, 3, 8],[9, 5, 1],[2, 7, 6]],
    [[8, 1, 6],[3, 5, 7],[4, 9, 2]],
    [[6, 7, 2],[1, 5, 9],[8, 3, 4]],
    [[2, 9, 4],[7, 5, 3],[6, 1, 8]]]

def sub(A, B):
    cost = 0
    for i in range(3):
        for j in range(3):
            cost += abs(A[i][j]-B[i][j])
    return cost

def formingMagicSquare(A):
    costs = map(lambda B: sub(A, B), M)
    return min(costs)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
