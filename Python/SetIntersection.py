# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
english = set(input().split())
b = input()
french = set(input().split())

both = english.intersection(french)
print(len(both))

