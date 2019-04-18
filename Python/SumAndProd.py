import numpy

n,m = map(int, input().split())
nm = numpy.array([input().split() for _ in range(n)], int)

print(numpy.prod(numpy.sum(nm, axis=0)))
