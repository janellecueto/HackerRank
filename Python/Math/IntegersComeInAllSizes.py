# Enter your code here. Read input from STDIN. Print output to STDOUT
a,b,c,d = map(int, [input() for _ in range(4)]) #since we know there will only be a, b, c, and d, we can use list comprehension to grab the input
print(a**b+c**d)

