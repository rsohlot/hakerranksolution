#problem: https://www.hackerrank.com/challenges/divisible-sum-pairs


#solution:


#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    all_combination  = list(itertools.combinations(ar, 2))
    counter = 0
    for each_combination in all_combination:
        if sum(list(each_combination)) % k == 0:
            counter+=1

    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
