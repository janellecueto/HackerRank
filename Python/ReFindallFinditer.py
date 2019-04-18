# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

S = input()
m = re.findall(r"(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})[qwrtypsdfghjklzxcvbnm]", S, re.I)
print("\n".join(m or ['-1']))
