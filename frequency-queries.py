# Question : https://www.hackerrank.com/challenges/frequency-queries

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    result =[]
    data = {}
    
    for (i,j) in queries:
        if i == 1:
            data[j] = data.get(j,0) + 1
        if i == 2 and i in data.keys():
            data[j] = data[j] - 1
        if i == 3:
            if j in data.values():
                result.append(1)
            else:
                result.append(0)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
