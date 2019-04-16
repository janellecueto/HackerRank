import re

if __name__ == '__main__':
    s = input()
    print(bool(re.search(r'\w', s)))  #alphanumeric
    print(bool(re.search("[A-Za-z]", s)))   #has letters
    print(bool(re.search(r'\d', s))) #has numbers
    print(bool(re.search("[a-z]", s)))  #has lowercase
    print(bool(re.search("[A-Z]", s)))  #has uppercase
