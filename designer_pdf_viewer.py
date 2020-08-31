# problem : https://www.hackerrank.com/challenges/designer-pdf-viewer/problem


#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    alp = 97
    maping = {}
    for e_h in h:
        maping[chr(alp)] = e_h
        alp+=1
    max_h = 0
    for i in word:
        if maping[i] > max_h:
            max_h = maping[i]
        
    area = len(word) * max_h
    return area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
