# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

if len(set(input().split())) == n:
    print("YES")
else:
    print("NO")

