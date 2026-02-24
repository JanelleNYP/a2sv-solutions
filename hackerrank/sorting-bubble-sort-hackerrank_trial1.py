#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    n = len(a)
    numSwaps = 0
    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a [j + 1] = a[j + 1], a[j]
                numSwaps += 1
                
        firstElement = a[0]
        lastElement = a[n - 1]
                
    print(f"Array is sorted in {numSwaps} swaps.")
    print(f"First Element: {firstElement}")
    print(f"Last Element: {lastElement}")
            
            
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)