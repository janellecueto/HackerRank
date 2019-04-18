#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    hr = int(s[0:2])
    if s[-2] == 'P':
        if hr == 12:
            return str(hr)+s[2:-2]
        return str(hr+12)+s[2:-2]
    else:
        if hr == 12:
            return "00"+s[2:-2]
        return s[0:-2]


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

