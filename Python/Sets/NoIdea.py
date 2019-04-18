# Enter your code here. Read input from STDIN. Print output to STDOUT

nm = input().split()
n = nm[0]   #number of elements in array
m = nm[1]   #number of elements in a and b 

arr = input().split()
happy = set(input().split())
unhappy = set(input().split())

happiness = 0
for a in arr:
    if(a in happy):
        happiness = happiness + 1
    if(a in unhappy):
        happiness = happiness - 1

print(happiness)
