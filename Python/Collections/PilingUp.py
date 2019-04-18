# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

T = int(input())
for _ in range(T):
    num = int(input())
    cubes = deque(map(int, input().split()))    #using a deque allows for popping from both sides of a list 
    last = 2**37
    while len(cubes) > 1:
        if cubes[0] >= cubes[-1] and cubes[0] <= last:      #make sure the outer bounds are always >= than everything else in cubes
            last = cubes.popleft()                          #and that they are <= the last cube we saw
        elif cubes[-1] > cubes[0] and cubes[-1] <= last:
            last = cubes.pop()
        else:
            print("No")
            break
    if len(cubes) == 1:
        print("Yes")
