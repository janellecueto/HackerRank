#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = Counter(input())
    l = sorted(s.items(), key=lambda x: (-x[1], x[0]))
    for i in range(3):
        print(l[i][0] + " " + str(l[i][1]))
