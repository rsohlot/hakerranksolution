##problem : https://www.hackerrank.com/challenges/drawing-book

### Code logic needs improvement.
##solution:

#!/bin/python3
'''
* page 1 is always on Right side. So, combination of pages will be (,1),(2,3),(4,5),(6,7)...(even,odd)
* n = total number of pages,i.e., last page number
* p = page number to turn on.


* If we consider, teacher flips one pages at a time.Then, It requires less flips
	1. From front,if p < n/2 (preivious then middle of the book)
	2. From back, if p > n/2 

* To get to page 2 it takes 1 flip, to page 4 it takes 2 flips,to page 6 it takes 3 flips so on...
	It takes p/2 flips. 
'''
import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    ### page to go is beyond the middle of the book
    if p > n/2 :
        if n-1 == p: return 1
        return int((n-p)/2)
    else:
        return int(p/2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
