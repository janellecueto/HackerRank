# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

S = input()
m = re.search(r"([a-zA-Z0-9])\1+", S)
print(m.group(1) if m else -1)

