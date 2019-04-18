# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
setn = set(input().split())

b = int(input())
setb = set(input().split())

sets = setn.union(setb)
print(len(sets))

