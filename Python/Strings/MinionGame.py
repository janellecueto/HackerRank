vowels = ['A', 'E', 'I', 'O', 'U']
def ret_points(string, mset):
    points = 0
    for m in mset:
        points += string.count(m)
    return points

def minion_game(string):
    # your code goes here
    stuart = 0
    kevin = 0
    strlen = len(string)
    #iterate through each char in the string
    for i in range(strlen):
        if string[i] in vowels:     #words starting with vowels go to kevin
            kevin += 1              #add this word to kevin's count
            kevin += strlen - i - 1     #all substrings beginning with this letter go to kevin's count
        else:                           #   ex. BANANA
            stuart += 1                 #        ^
            stuart+= strlen - i - 1     #   at this point in the string, kevin gets ANANA and ANAN, ANA, AN, A
    #now check who's won
    if stuart > kevin:
        print("Stuart "+str(stuart))
    elif stuart == kevin:
        print("Draw")
    else:
        print("Kevin "+str(kevin))
    



if __name__ == '__main__':
    s = input()
    minion_game(s)
