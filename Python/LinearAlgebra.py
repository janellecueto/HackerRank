import numpy
numpy.set_printoptions(legacy='1.13')   #this is set  only to match the required format for the challenge.

N = int(input())
A = [[float(a) for a in input().split()] for _ in range(N)]
print(numpy.linalg.det(A))
