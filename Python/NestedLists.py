from operator import itemgetter

def takeSecond(elem):
    return elem[1]

if __name__ == '__main__':

    l = []
    s = set()
    T = int(input())
    for _ in range(T):
        name = input()
        score = float(input())
        l.append([name, score])
        s.add(score)
    
    l.sort(key=itemgetter(1,0))
    ss = list(s)
    ss.sort(key=float)
    last = ss[1]
    i = 0
    if T > 2:
        i = 1

    for sub in l[i:]:
        if sub[1] == last: 
            print(sub[0])
