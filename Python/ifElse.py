#!/bin/python3

N = int(input())
if N%2:
    print("Weird")
else:
    if N in range(6,21):
        print("Weird")
    else:
        print("Not Weird")