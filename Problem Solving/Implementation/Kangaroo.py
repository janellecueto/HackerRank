#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if v2 >= v1:                        #basically, we are solving X for v1X + x1 = v2X + x2
        return "NO"                     #   restricting x to be a whole number. 
    if (x1-x2)%(v2-v1) != 0:            #   v1X + x1 - x2 = v2X
        return "NO"                     #   x1 - x2 = v2X - v1X
    else:                               #   x1 - x2 = (v2-v1)X
        return "YES"                    #   (x1 - x2)/(v2 - v1) = X where (x1 - x2)%(v2 - v1) is 0 so that X is a whole number

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
