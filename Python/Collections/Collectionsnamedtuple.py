# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

n = int(input())
Spread = namedtuple("Spread", input().split())      #create Spread from first line denoting column names
marks = [int(Spread._make(input().split()).MARKS) for _ in range(n)]    #this makes each line a Spread then takes the MARKS from the line to add to marks
print(sum(marks)/n)
