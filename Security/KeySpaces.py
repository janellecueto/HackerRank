# Enter your code here. Read input from STDIN. Print output to STDOUT
K = [0,1,2,3,4,5,6,7,8,9] #sorted list of digits that will use the input digits as indices 

digits = input()
step = int(input())

for d in digits:
    index = int(d)
    if index > (9-step): #this accounts for overflow so we wrap around to the beginning of K
        index -= 10
    print(K[index+step], end="")

