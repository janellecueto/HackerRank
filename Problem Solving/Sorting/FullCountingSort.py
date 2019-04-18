#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    #first half are dashes
    counts = [[] for _ in range(100)]       #list of 100 empty lists (x <= 100 for "<int x> <string s>" from input arr)
    half = len(arr)/2
    i = 0
    for x,s in arr:
        if i < half:
            counts[int(x)].append("-")      #first half of arr from input gets converted to '-'
        else:
            counts[int(x)].append(s)        
        i+=1
    flatten = [j for sub in counts for j in sub]
    # print(flatten)
    print(" ".join(flatten))

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
