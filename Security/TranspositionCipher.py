# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def decode(string):
    #here, i will create the "alphabet" decoder
    l = {}  #this holds a dictionary of columnized letters based on string
    keyword = "".join(sorted(set(string), key=string.index))
    strlen = len(keyword)
    rem_alpha = [a for a in alphabet if a not in string]    #remaining letters from alphabet not included in set string (keyword)
    #populate the dictionary
    for i in range(strlen):
        l[keyword[i]] = [(rem_alpha[j]) for j in range(i, len(rem_alpha), strlen)]
    #convert dictionary sorted by key to flattened list 
    llist = []
    for key in sorted(l):
        llist.append(key)
        for v in l[key]:    #go down the columns 
            llist.append(v)
    #create a new dictionary where the alphabet is mapped to llist
    decoder = {}
    for i in range(26):
        decoder[llist[i]] = alphabet[i]
    return decoder


n = int(input())

for _ in range(n):
    key = input()
    msg = input()
    decoder = decode(key)   #create a decoder dictionary to decrypt the message
    printstr = ''
    for m in msg:
        if m in decoder.keys():
            printstr += decoder[m]
        else:
            printstr += " "
    print(printstr)


