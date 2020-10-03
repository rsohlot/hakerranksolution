# problem: https://www.hackerrank.com/challenges/circular-array-rotation/problem
'''
solution
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):

    if k > len(a):
        k = k % len(a)
    result = []
    for i in queries:
        # the blocks those where shifted to front after rotation
        # len - rotation - 1 is shifted to zeroth index
        if i < k:
            result.append(a[len(a) - k + i])
        else:
            result.append(a[i - k])
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
