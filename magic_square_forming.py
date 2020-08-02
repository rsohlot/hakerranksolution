#problem: https://www.hackerrank.com/challenges/magic-square-forming

## solution: 


'''
possible combination for the soluton:
[8, 1, 6,   [2, 9, 4,
 3, 5, 7,	 7, 5, 3,
 4, 9, 2],   6, 1, 8],         
             
[6, 1, 8,	[8, 3, 4,
 7, 5, 3,  	 1, 5, 9,
 2, 9, 4],	 6, 7, 2],

[4, 9, 2,	[4, 3, 8,
 3, 5, 7,	 9, 5, 1, 
 8, 1, 6],	 2, 7, 6],
            
 [6, 7, 2,  [2, 7, 6,
 1, 5, 9,  	9, 5, 1,
 8, 3, 4],   4, 3, 8]         
              
             
             
Check for each matrix and find the minimum cost.

'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    n_s = []
    for i in range(len(s)):
        for j in range(len(s[i])):
            n_s.append(s[i][j])
    s = n_s
    all_n = [
            [8, 1, 6, 3, 5, 7, 4, 9, 2],
            [6, 1, 8, 7, 5, 3, 2, 9, 4],
            [4, 9, 2, 3, 5, 7, 8, 1, 6],
            [2, 9, 4, 7, 5, 3, 6, 1, 8],
            [8, 3, 4, 1, 5, 9, 6, 7, 2],
            [4, 3, 8, 9, 5, 1, 2, 7, 6],
            [6, 7, 2, 1, 5, 9, 8, 3, 4],
            [2, 7, 6, 9, 5, 1, 4, 3, 8]
        ]
    allsum = []
    for l in all_n:
        allsum.append(sum([abs(s[i]-l[i]) for i in range(9)]))
    return min(allsum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
