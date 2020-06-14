##problem:  https://www.hackerrank.com/challenges/electronics-shop

'''
* If min price of mouse and keyboard is greater than budget then return -1.
* If the price of mouse and keyboard less than budget - max(keyboard) and budget - max(mouse) are no need to compare.
'''

##solution: 

#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    
    if min(keyboards)+ min(drives) > b:
        return -1
    max_spend = 0
    for k in keyboards:
        for d in drives:
            if k+d <= b and k+d > max_spend:
                max_spend = k+d
    return max_spend

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
