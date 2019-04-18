# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

items = OrderedDict()
for _ in range(int(input())):
    item = input().rpartition(" ") #rpartition - breaks string by last occurence 
    items[item[0]] = items.get(item[0],0) + int(item[-1]) 
for i, q in items.items():
    print(i, q)
