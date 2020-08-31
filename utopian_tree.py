# problem: https://www.hackerrank.com/challenges/utopian-tree/problem


'''
solution:

sequence :
x 2x 2x+1 4x+2 4x+3 8x+6 8x+7 16x+14 16x+15 

0  1   2    3    4    5   6     7     8

in our case x =1


so 

n for even : 2^(n/2) x+ n-1


n for odd : 2^(n/2) x+ n-2
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    result = 0
    if n == 0:
        return 1
    if n == 1:
        return 2
    pwr = int(math.pow(2,int(n/2)))
    if n%2 == 0:
        result = pwr + pwr-1
    else:   
        result = int(math.pow(2,int((n+1)/2))) + int(math.pow(2,int((n+1)/2))) -2
    
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
