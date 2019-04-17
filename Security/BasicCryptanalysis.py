# Enter your code here. Read input from STDIN. Print output to STDOUT

#this function checks if two strings have a one-to-one mapping of characters
def isomorphic(e, s):
    #e and s are going to be the same len
    elen = len(e)
    marked = [False] * 256  #this keeps track of our spot in s 
    mmap = [-1] * 256       #this keeps track of the letter in s that the letter in e is mapped to 
    for i in range(elen):
        if mmap[ord(e[i])] == -1:           #when we visit a char in e that hasn't been mapped,
            if marked[ord(s[i])] == True:   #   if that char is already marked (we already saw the char in s)
                return False                #       then e and s are not isomorphic
            marked[ord(s[i])] = True        #   else    mark the char in s as visited
            mmap[ord(e[i])] = s[i]          #           map the char in e to the char in s
        elif mmap[ord(e[i])] != s[i]:       #if the char in e has been mapped but the char in s is not its mapping,
            return False                    #   then the strings are not isomorphic
    return True

#this function scores how well the word in question and the supposed match compare to the alphamap dictionary 
def score(word, match):
    score = 0
    #word and match will be same length and isomorphic
    mmap = {}
    for i in range(len(word)):
        mmap[word[i]] = match[i]
    for key in mmap.keys():
        if mmap[key] == alphamap[key]:
            score += 1                      #if there is a mapping in alphamap for the char in word, add to the score
    return score

#this function adds letter mappings in the alphamap dictionary (without rewriting previously added mappings)
def add_pair(word, match):
    for i in range(len(word)):
        if alphamap[word[i]] == -1:
            alphamap[word[i]] = match[i]


# words are contained in dictionary.lst 
f = open("dictionary.lst", "r")
l = []
for x in f:
    l.append(x.lower().strip())     #list l contains all of our dictionary words

encoded = list(input().split())     #list encoded contains all of the words we need to match 
master = {}                     #words may have more than one mapping in the dict, master is a dictionary where the key is the 
for e in encoded:               #word in encoded[] and the value is a list of all possible matches from l (dictionary.lst)
    elen = len(e)
    mini = [x for x in l if len(x) == elen] #break list into list of words of same length
    words = []
    for m in mini:
        if isomorphic(e, m):                #check if those words are isomorphic
            words.append(m)                 #if they are, add the the list of possible word matches
    master[e] = words           


alpha = 'abcdefghijklmnopqrstuvwxyz'
alphamap = {}
for a in alpha:
    alphamap[a] = -1        #initialize our encryption/decription dictionary by mapping the alphabet to -1 (meaning the letter has no match yet)

for word in sorted(master, key=lambda k: len(master[k])):       #sort the master dictionary by word length
    if len(master[word]) == 1:                                  #if there's one match for a word (value list only contains 1 word), 
        match = master[word][0]                                 #   then that's the correct mapping
        add_pair(word, match)
        master[word] = match
    #if it's greater than 1, we score based on current alphamap then remove lowest scores
    else:
        max_score = 0
        max_match = ''
        for m in master[word]:
            s = score(word, m)
            if s > max_score:
                max_score = s
                max_match = m
        master[word] = max_match            #word now has one match
        add_pair(word, max_match)

#after this is all done, we have a one to one matching 
print(" ".join([master[e] for e in encoded]))
