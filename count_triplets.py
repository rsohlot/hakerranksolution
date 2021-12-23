# qustion ; https://www.hackerrank.com/challenges/count-triplets-1/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import OrderedDict

# Python Program to Print
# all subsets of given size of a set
 
import itertools
 
def findsubsets(s, n):
    return list(itertools.combinations(s, n))


def isPerfectSquare(x):
    #if x >= 0,
    if(x >= 0):
        sr = math.sqrt(x)
        # sqrt function returns floating value so we have to convert it into integer
        #return boolean T/F
        return (round((sr*sr),2) == round(float(x),2))
    return False

    
# Complete the countTriplets function below.
def countTriplets(arr, r):
    valid_numbers = []
    valid_numbers_log = []
    for i in arr:
        if isPerfectSquare(i):
            if r == 1:
                # will throw zero division error in else for r == 1
                valid_numbers_log.append(int(i))
            else:
                valid_numbers_log.append(int(math.log(i,r)))
    
    numbers_subset = findsubsets(valid_numbers_log, 3)
    result = 0
    for i,j,k in numbers_subset:
        if r == 1 and j - i == 0 and k - j == 0:
            result += 1
        elif r != 1 and  j - i == 1 and k - j == 1:
            result += 1
            
    return result


    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
 
