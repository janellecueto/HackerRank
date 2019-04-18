import numpy

nm = input().split()
n = int(nm[0])
m = int(nm[1])

master = []
for i in range(n):
    master.append([int(x) for x in input().split()])
mins = numpy.min(master, axis=1)
print(numpy.max(mins))
