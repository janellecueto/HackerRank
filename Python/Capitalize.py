#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    if re.search('\d[a-z]', s):     #this search captures any string with words containing numbers and letters. (ex. 23b, 1defg, etc)
        ss = [n[0].upper() + n[1:] for n in s.split()]      #only capitalize the first char in each word 
        return " ".join(ss)
    else:
        return s.title()            #otherwise .title() will capitalize the first letter of each word


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

