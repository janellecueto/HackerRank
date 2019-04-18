#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level = 0       #everytime we reach level, we look to the next step to determine valley
    inval = False
    valleys = 0
    for c in s:
        print(level)
        if c == 'U':
            level += 1
        elif c == 'D':
            level -= 1
        if level == -1 and inval == False:
            print("in valley ")             #these statements print to debug output
            valleys += 1
            inval = True
        if level == 0 and inval == True:
            #we've come out of a valley
            print("out valley")
            inval = False
        
    return valleys
            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
