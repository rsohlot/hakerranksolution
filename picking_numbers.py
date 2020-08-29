## problem : https://www.hackerrank.com/challenges/picking-numbers/problem?isFullScreen=false



'''
solution:
As the diff. can be 1 between any 2 numbers,so the numbers in a list can be n and n+1/n-1.
So, create the all possible pair of numbers. and check the max len of list.
Then compare the pair's len with the individual number's len.
eg:
[4,5,4,5,50,50,50,50,50]
here max len will be 5 for list [50,50,50,50,50]
'''

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
import collections
#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    c = Counter(a)
    od = collections.OrderedDict(sorted(c.items()))
    pairs = []
    ks = list(od.keys())
    for v in range(len(ks)):
        for j in range(v,len(ks)):
            if ks[v] !=ks[j] and abs(ks[v]-ks[j]) <=1:
                pairs.append((ks[v],ks[j]))
    max_len = 0
    for f,s in pairs:
        new_len = od.get(f) + od.get(s)
        if new_len > max_len:
            max_len = new_len

    for k,v in od.items():
        if v > max_len:
            max_len = v

    return max_len


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
