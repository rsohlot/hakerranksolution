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
from bisect import bisect_right

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    # the earlier loop was in time out condition for 2L size of scores len.
    scores = sorted(set(scores))
    rank = []
    for i in alice:
        rank.append(len(scores)-bisect_right(scores,i)+1)

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
