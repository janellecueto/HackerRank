import numpy

N = int(input())
A = []
B = []
for i in range(N):
    A.append(numpy.array(input().split(), int))
for j in range(N):
    B.append(numpy.array(input().split(), int))

print(numpy.dot(A,B))
