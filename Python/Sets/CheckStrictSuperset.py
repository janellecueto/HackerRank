# Enter your code here. Read input from STDIN. Print output to STDOUT

A = set(input().split())
N = int(input())
for _ in range(N):
    if not A.issuperset(set(input().split())):
        print("False")
        exit(0)
print("True")
