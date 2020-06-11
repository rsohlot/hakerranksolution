#problem : https://www.hackerrank.com/challenges/the-birthday-bar/

#solution:

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    import itertools
    iterable = s
    r = m
    count_successful_combination = 0
    ## itertools combination returns all the combination
    # all_combinations = list(itertools.combinations(iterable, r))
    all_combinations = [iterable[i:i+r] for i in range(len(iterable)-r+1) ]
    for each_combination in all_combinations:
        if sum(list(each_combination)) == d:
            print(each_combination)
            count_successful_combination+=1
    return count_successful_combination

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
