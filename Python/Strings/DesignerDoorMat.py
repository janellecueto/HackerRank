# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    nm = input().split()
    N = int(nm[0])
    M = int(nm[1])
    for i in range(1,N, 2):
        print((".|."*i).center(M, "-"))
    print("WELCOME".center(M, "-"))
    for j in range(1, N, 2):
        print((".|." * (N-j-1)).center(M, "-"))
