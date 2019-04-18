import numpy
numpy.set_printoptions(legacy='1.13')

N, M = map(int, input().split())
master = []
for i in range(N):
    master.append(numpy.array(input().split(), int))
print(numpy.mean(master, axis=1))
print(numpy.var(master, axis=0))
print(numpy.std(master))
