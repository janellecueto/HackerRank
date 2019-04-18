#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for i in range(1,n):
        curr = arr[i]
        j = i-1
        while j >=0 and arr[j] > curr:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = curr
        print(" ".join(map(str, arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
