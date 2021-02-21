# Problem: https://www.hackerrank.com/challenges/library-fine/problem


# Soltion:
#!/bin/python3

import math
import os
import random
import re
import sys

from datetime import date

# Complete the libraryFine function below.
def libraryFine(d1, m1, y1, d2, m2, y2):
    fine = 0
    returned_date = date(y1, m1, d1)
    due_date = date(y2, m2, d2)
    delta =  due_date - returned_date
    if delta.days >=0:
        return fine
    if m2 == m1 and y1 == y2 :
        fine = 15 * abs(delta.days)
    if y1 == y2 and m1 != m2:
        fine = 500 * abs((returned_date.year - due_date.year) * 12 + (returned_date.month - due_date.month))
    if y2!= y1 :
        fine =  10000
    return fine

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    d1M1Y1 = input().split()

    d1 = int(d1M1Y1[0])

    m1 = int(d1M1Y1[1])

    y1 = int(d1M1Y1[2])

    d2M2Y2 = input().split()

    d2 = int(d2M2Y2[0])

    m2 = int(d2M2Y2[1])

    y2 = int(d2M2Y2[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()
