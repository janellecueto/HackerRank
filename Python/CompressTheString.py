# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

S = input()

groups = [list(g) for k, g in groupby(S)]
tups = []
for g in groups:
    tups.append((len(g), int(g[0])))
for t in tups:
    print(t, end=" ")

