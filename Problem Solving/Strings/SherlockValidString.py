#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    scount = Counter(s)                     # dictionary of each char in s mapped to their counts
    print(scount)                           # (prints to debug output)
    comCounts = Counter(scount.values())    # dictionary of counts to their counts ex. {a:2, b:2, c:2, d:1} -> {2:3, 1:1}
    prev = comCounts.most_common(1)[0][0]   
    different = 0
    only1 = False
    print(prev)
    for b in scount.values():               # NOTE: I could have just checked for the length of counts and most_common count: 
        if b != prev:                       #       - if there were more than 2, automatic "NO", but if 1, "YES"
            if not only1:                   #       - if the other count happened more than once, "NO"
                only1 = True                #       - if the other count is greater than the most common by over 1, "NO"
                different = b               #       - if the other count is less than the most common, "NO"
            else:
                return "NO"
    if different == 1 or different == 0:
        return "YES"
    if abs(different - prev) > 1:
        return "NO"
    return "YES"

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

