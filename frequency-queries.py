# Question : https://www.hackerrank.com/challenges/frequency-queries

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    result =[]
    data = defaultdict(int)
    
    for (i,j) in queries:
        if i == 1:
            data[j] = data.get(j,0) + 1
        if i == 2 and j in data.keys() and data.get(j) >= 1:
            data[j] = data[j] - 1
        if i == 3:
            ans = 0
            if j in data.values():
                ans = 1
            result.append(ans)
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
