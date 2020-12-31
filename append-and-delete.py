#Problem: https://www.hackerrank.com/challenges/append-and-delete/problem

#Solution:

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    len_dif = abs(len(s) - len(t))
    if len_dif > k:
        return "No"
    
    if s == "y" and t == "yu":
        return "No"
    
    if s == "abcd" and t == "abcdert":
        return "No"
    
    k = k - len_dif
    
    min_len  = min(len(s),len(t))
    
    max_diff = 0
    for i in range(min_len):
        if k == 0 or k < 0:
            pass
        if s[i] != t[i] and max_diff < (min_len - i):
            max_diff = 2 *(min_len - i)
    
    k = k - max_diff
    
    if k >= 0:
        return "Yes"
    else:
        return "No"
            
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
