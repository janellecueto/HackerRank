# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

N = int(input())
l = input().split()
K = int(input())
perms = combinations(l, K)      #all combinations in l of size k

count = 0
size = 0
for p in perms:
    size += 1                   #this is really just len(perms)
    if 'a' in p:                #if there is an 'a' in the tuple, add to count
        count += 1
print(count/size)
