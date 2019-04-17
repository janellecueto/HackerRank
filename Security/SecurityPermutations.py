# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

arr = list(map(int, input().split()))
for i in range(n):
    j = arr[i]
    print(arr[j-1])

