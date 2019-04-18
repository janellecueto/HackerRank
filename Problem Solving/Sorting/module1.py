#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort function below.
# this is my insertion sort algorithm from previous challenges
def insertionSort(arr):
    n = len(arr)        
    shifts = 0
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
            shifts += 1
        arr[j+1] = key
    return shifts

# helper function that gets sum of bitree
def getSum(bitree, index):
    s = 0
    while index > 0:
        s += bitree[index]
        index -= index & (-index)   #if index is odd, -= 1, else -= lowest bit
    return s
# helper function for filling up the bitree
def updateBit(bitree, n, index, val):
    while index <= n:
        bitree[index] += val
        index += index & (-index)   #ex. for index=1, index = 1 + (01 & ~01) = 1 + (01 & 11) = 2
                                    #                 index = 2 + (010 & ~010) = 2 + (010 & 110) = 4
def countShifts(arr, n):
    shifts = 0
    mx = max(arr)
    bitree = [0] * (mx+1)           # bitree will hold the number of elements before arr[i] that are greater than arr[i]
    for i in range(n-1, -1, -1):
        shifts += getSum(bitree, arr[i]-1)
        updateBit(bitree, mx, arr[i], 1)
    return shifts

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countShifts(arr, n)        # rather than counting shifts in the insertion sort algorithm, we can use a Binary Indexed Tree
                                            # as suggested in the Discussions tab
        fptr.write(str(result) + '\n')

    fptr.close()
