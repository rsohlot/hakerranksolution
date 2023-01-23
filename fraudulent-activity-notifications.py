# problem : https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    # Write your code here
    notification_count = 0
    for i in range(d,len(expenditure)):
        ordered_past_transaction = sorted(expenditure[i-d:i])
        median_amount = 0
        if d%2 == 0:
            median_amount = (ordered_past_transaction[int((d/2)-1)] +               ordered_past_transaction[int(d/2)])/2
        else:
            median_amount = (ordered_past_transaction[int(d/2)]) 
            
        
        # check if new transaction amount is greater than trailing median
        if expenditure[i] >= 2 * median_amount:
            notification_count += 1
    
    return notification_count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
