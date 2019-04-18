def print_rangoli(size):
    # your code goes here
    off = 4 * (size-1) + 1
    string = ""
    for i in range(1, size+1):
        for j in range (0, i):
            string += chr(96+size-j)
            if len(string) < off:
                string += '-'
        for k in range(i-1, 0, -1):
            string += chr(97+size-k)
            if len(string) < off:
                string += '-'
        print(string.center(off, '-'))
        string = ""
    for i in range(size-1, 0, -1):
        for j in range(0, i):
            string += chr(96+size-j)
            if len(string) < off:
                string += '-'
        for k in range(i-1, 0, -1):
            string += chr(97+size-k)
            if(len(string)<off):
                string += '-'
        print(string.center(off, '-'))
        string = ""
#NOTE:
#   A shorter solution can be achieved by using a list of alphabet characters and slicing that list based on an index and n



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
