def merge_the_tools(string, k):
    # your code goes here
    l = []
    for i in range(0, len(string), k):      #string= AABCAAADA
        l.append(string[i:i+k])             #l = [AAB, CAA, ADA]
    for j in l:
        c = ''
        for a in range(k):                  
            if j[a] not in c:               #to remove multiples:
                c += j[a]
        print(c)
            


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
