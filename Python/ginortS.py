# Enter your code here. Read input from STDIN. Print output to STDOUT

c = input()

print(''.join(sorted(c, key=lambda x:(x.isdigit() - x.islower(), x in '02468', x))))
#sort string by chars first (lower then upper before all digits), then evens, then the rest (odds)
