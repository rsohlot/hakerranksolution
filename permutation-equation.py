# Problem: https://www.hackerrank.com/challenges/permutation-equation/problem

'''
solution:
find the value in reverse, iterate the array and find what is at the value index.
'''

#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the permutationEquation function below.
def permutationEquation(p):
    result = {}
    # key is the value of x and value will be the value
    for i in p:
        result[p[p[i-1]-1]] = i
    od = collections.OrderedDict(sorted(result.items()))
    return od.values()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
