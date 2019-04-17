# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

arr = list(map(int, input().split()))

for i in range(n):
    try:
        assert i + 1 == arr[arr[i]-1]  #pretend arr is f, i+1 == f(f(i)-1) because arr is zerobased where as the problem starts at 1
    except IndexError:
        print("NO")
        exit(0)
    except:
        print("NO")
        exit(0)
print("YES")
