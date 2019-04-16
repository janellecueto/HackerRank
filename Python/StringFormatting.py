def print_formatted(number):
    # your code goes here
    offset = len(str(bin(number))[2:])
    for i in range(1, number+1):
        b = str(bin(i))[2:]
        o = str(oct(i))[2:]
        h = str(hex(i))[2:]
        print(str(i).rjust(offset)+" "+o.rjust(offset)+" "+h.upper().rjust(offset)+" "+b.rjust(offset))
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
