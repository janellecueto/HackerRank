if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    ls = list(set(arr))
    ls.sort(key=int)
    print(ls[len(ls)-2])