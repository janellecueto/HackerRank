# Enter your code here. Read input from STDIN. Print output to STDOUT

nx = input().split()
x = int(nx[1])

grades = []
for i in range(x):
    grades.append(map(float,input().split()))

zipped = zip(*grades)
for z in zipped:
    print("{:.1f}".format(sum(z)/len(z)))

