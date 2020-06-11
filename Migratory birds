#problem: https://www.hackerrank.com/challenges/migratory-birds

##solution:

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    
    freq = Counter(arr)
    id_max_count = [k for k,v in freq.items() if v == max(freq.values())]

    return min(id_max_count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
