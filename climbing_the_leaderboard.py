# problem: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

'''
Solution:
'''
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
import collections

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    c= Counter(scores)
    od = collections.OrderedDict(sorted(c.items(),reverse=True))

    rank = []
    rank_found = False
    for a_s in alice:
        counter = 0
        for s in od:
            counter+=1
            if a_s >= s:
                rank_found = True
                rank.append(counter)
                break
        if not rank_found:
            rank.append(counter+1)

    return rank

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
