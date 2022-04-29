#!/bin/python3
# Question : https://www.hackerrank.com/challenges/count-triplets-1

import math
import os
import random
import re
import sys

# help : https://youtu.be/KZ8k9-22JmQ
def countTriplets(arr, r):
    before = {}
    after = {}
    for i in arr:
        if i in arr:
            after[i] += 1
        else:
            after[i] = 1
            
    count = 0
    for i in arr:
        after[i] -= 1
        if i//r in before and i %r == 0 and i*r in after:
            count += before[i//r] * after[i*r]
        if i in before:
            before[i] += 1
        else:
            before[i] = 1
        
    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
 
