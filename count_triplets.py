#!/bin/python3

import math
import os
import random
import re
import sys
from collections import OrderedDict

import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom  # or / in Python 2

# Python Program to Print
# all subsets of given size of a set
 
import itertools
 
def findsubsets(s, n):
    return list(itertools.combinations(s, n))


def isPerfectSquare(x):
    #if x >= 0,
    if(x >= 0):
        sr = math.sqrt(x)
        # sqrt function returns floating value so we have to convert it into integer
        #return boolean T/F
        return (round((sr*sr),2) == round(float(x),2))
    return False

    
# Complete the countTriplets function below.
def countTriplets(arr, r):
    each_number_index = {}
    number_combunation = {}
    index = -1
    first_value = arr[0]
    result_for_zero = 0
    for i in arr:
        index += 1
        if isPerfectSquare(i):
            if r == 1 and i == first_value:
                # will throw zero division error in else for r == 1
                result_for_zero += 1
            else:
                i = int(math.log(i,r))
                # add each number to the dictionary
                if i in each_number_index:
                    each_number_index[i] = each_number_index[i] + [index]
                else:
                    each_number_index[i] = [index]
                # add to the dictionary the number of combinations, if possible
                if i-1 in each_number_index:
                    combination = len(each_number_index[i-1])
                    if (i-1,i) in number_combunation.keys():
                        print('----------',number_combunation[(i-1,i)])
                        number_combunation[(i-1,i)] = number_combunation[(i-1,i)] + [combination]
                        print(number_combunation[(i-1,i)])
                    else:
                        number_combunation[(i-1,i)] = [combination]
    
    result = 0
    if r == 1:
        result = ncr(result_for_zero,3)
    else:
        print(number_combunation)
        print(number_combunation.keys())
        for i in number_combunation:
            i,j = i
            if (i-1,j-1) in number_combunation.keys():
                print('------',i,j)
                previous_combination = number_combunation[(i-1,j-1)]
                for idx in number_combunation[(i,j)]:
                    print(idx)
                    filtered_list = previous_combination[:idx+1]
                    print(filtered_list)
                    result += sum(filtered_list)

    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
 
