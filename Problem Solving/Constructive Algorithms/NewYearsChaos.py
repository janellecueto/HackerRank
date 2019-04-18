#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    lenq = len(q)
    numBribes = 0
    for i in range(lenq):
        pos = i+1
        badge = q[i]
        bribes = badge - pos
        if bribes > 2:
            print("Too chaotic")
            return
        for j in range(max(badge-2, 0),pos):
            if q[j] > badge:
                numBribes += 1
        
    print(numBribes)
        


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
