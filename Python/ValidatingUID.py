# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    t = ''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}', t)
        assert re.search(r'\d\d\d', t)
        assert not re.search(r'[^a-zA-Z0-9]', t)
        assert not re.search(r'(.)\1', t)
        assert len(t) == 10
    except:
        print("Invalid")
    else:
        print("Valid")
