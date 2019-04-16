# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

S, k = input().split()

S = sorted(S)
k = int(k)

for h in list(permutations(S, k)):
    print("".join(h))

