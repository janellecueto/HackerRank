#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos, neg, zero = 0,0,0
    total = len(arr)
    for a in arr:
        if a == 0:
            zero += 1
        elif a > 0:
            pos += 1
        else:
            neg += 1
    print(pos/total)
    print(neg/total)
    print(zero/total)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
