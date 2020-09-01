# problem: https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

'''
solution:

We have create the reverse of a number by converting the number to a string and reversing it by sting[::-1]
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    beautiful_day = 0
    for i in range(i,j+1):
        if abs(i - int(str(i)[::-1])) % k == 0:
            beautiful_day +=1
        
    return beautiful_day
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
