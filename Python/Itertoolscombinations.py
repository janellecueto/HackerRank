# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

S, k = input().split()
k = int(k)
S = sorted(S)

for i in range(1, k+1):
    for j in list(combinations(S, i)):
        print("".join(j))

