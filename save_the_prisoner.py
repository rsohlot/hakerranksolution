# problem : https://www.hackerrank.com/challenges/save-the-prisoner/problem

'''
solution:
add the start of seat number to the number of candy to start always from seat 1.
Then, this will be a mod problem. Just find the reminder.
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    new_m = m + s - 1
    last = new_m % n
    if last == 0:
        return n
    return last

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
