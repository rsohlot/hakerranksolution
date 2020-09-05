# problem: https://www.hackerrank.com/challenges/strange-advertising/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    start = 5
    liked = 2
    cum_sum = 2
    for i in range(n-1):
        shared = liked*3
        liked = int(shared/2)
        cum_sum += liked
    return cum_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
