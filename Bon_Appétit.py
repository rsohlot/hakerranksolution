###problem:

##solution:
'''
bill = [list]
anna not eated = bill[k]
* correctly distributed, if (sum of bil about - k) /2 == anna have to pay. 
Else, else subract what anna has paid to (sum of bil about - k) /2 give the amout anna owes.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    anna_to_pay = (sum(bill) - bill[k]) / 2
    if b == anna_to_pay:
        print("Bon Appetit")
    else:
        print(int(b - anna_to_pay))


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)

