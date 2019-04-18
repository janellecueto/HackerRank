# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

X = int(input())
shoes = Counter(list(input().split()))

N = int(input())
money = 0
for i in range(N):
    #add price to money if shoe still exists
    size, price = input().split()
    if size in shoes.elements():
        money += int(price)
        shoes.subtract({size: 1})   #subtract from this size
print(money)
