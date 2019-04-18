def swap_case(s):
    retstr = ''
    for c in s:
        if c.islower():
            retstr += c.upper()
        elif c.isupper():
            retstr += c.lower()
        else:
            retstr += c
    return retstr

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
