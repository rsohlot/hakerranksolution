# Problem: https://www.hackerrank.com/challenges/cut-the-sticks/problem

# Solution:

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    total_count = len(arr)
    arr = dict(Counter(arr))
    arr_dict = dict([(i, arr[i]) for i in  sorted(arr.keys())])
    result= [total_count]
    new_len = total_count
    for i in arr_dict.keys():
        sub = i
        new_len = new_len - arr_dict[i]
        result.append(new_len)
    
    return result[:-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
