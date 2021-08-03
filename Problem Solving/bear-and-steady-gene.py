#!/bin/python3

import math
import os
import random
import re
import sys


def extras_available(all_counts, max_nucleotide_count):
    for counts in all_counts.values():
        if counts > max_nucleotide_count:
            return True
    return False

def steadyGene(gene):
    gene_length = len(gene)
    max_nucleotide_count = gene_length / 4
    all_counts = {
        "A": 0,
        "T": 0,
        "C": 0,
        "G": 0,
    }
    for nucleotide in gene: # O(n)
        all_counts[nucleotide] += 1
    if not extras_available(all_counts, max_nucleotide_count):
        return 0
    right_runner = 0
    left_runner  = 0
    min_substring_length = float("inf")
    while right_runner < gene_length:
        while right_runner < gene_length and extras_available(all_counts, max_nucleotide_count):
            nucleotide = gene[right_runner]
            all_counts[nucleotide] -= 1
            right_runner += 1
        while left_runner < gene_length and not extras_available(all_counts, max_nucleotide_count):
            nucleotide = gene[left_runner]
            all_counts[nucleotide] += 1
            left_runner += 1
        min_substring_length = min(min_substring_length, right_runner - left_runner + 1)
    return min_substring_length
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()
