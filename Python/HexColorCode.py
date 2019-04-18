# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N = int(input())

for i in range(N):
    codes = [j for j in re.findall('[\s:](#[a-f0-9]{3,6})', input(), re.I)]
    for code in codes:
        print(code)    
