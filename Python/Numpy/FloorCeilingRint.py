import numpy
numpy.set_printoptions(sign=' ')

A = numpy.array(input().split(), float)
print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))
