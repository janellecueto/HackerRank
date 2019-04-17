# Enter your code here. Read input from STDIN. Print output to STDOUT

alphabet = [0,1,2,3,4,5,6,7,8,9]
n = input()

for i in n:
    index = int(i) + 1
    if index > 9:
        index = 0
    print(alphabet[index], end="")
