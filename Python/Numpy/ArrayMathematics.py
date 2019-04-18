import numpy

n,m = map(int, input().split())
A = numpy.array([input().split() for _ in range(n)], int)
B = numpy.array([input().split() for _ in range(n)], int)

print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)
print(A**B)
