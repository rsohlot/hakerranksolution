##problem link: https://www.hackerrank.com/challenges/breaking-best-and-worst-records
##solution:


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    improved = 0
    falled = 0
    max_score = scores[0]
    min_score = scores[0]
    for s in scores:
        if s > max_score:
            improved+=1
            max_score = s
        if s < min_score:
            falled+=1
            min_score = s

    return improved,falled
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
