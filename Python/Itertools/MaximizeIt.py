# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

km = input().split()
K = int(km[0])
M = int(km[1])
master = []         #list of lists
for k in range(K):
    master.append(map(int, input().split()[1:]))    #master holds K lists of Ni elements 

carts = map(lambda x: sum(i**2 for i in x)%M, product(*master))     #first, find the cartesian product between the lists in master
                                                                    #the function we are mapping across the products is (x1**2 + x2**2 + ... + xNi)%M 
print(max(carts))                                                   #after the function has been mapped, we just find the max 
