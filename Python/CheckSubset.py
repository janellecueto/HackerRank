# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    a,A = input(), set(input().split())
    b,B = input(), set(input().split())
    if A.issubset(B):
        print("True")
    else:
        print("False")
