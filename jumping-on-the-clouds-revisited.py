# Problem: https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem

#Solution


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    score  = 100
    i = 0
    score_sub = { 0 : 1, 1: 3}
    # calculate the first jump
    i = (i+k)%len(c)
    score = score - score_sub.get(c[i])
    while score >= 0:
        if i == 0:
            break
        i = (i+k)%len(c)
        score = score - score_sub.get(c[i])
    return score
        

            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
