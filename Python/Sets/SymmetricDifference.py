# Enter your code here. Read input from STDIN. Print output to STDOUT

m = input()
m_set = set(input().split())
n = input()
n_set = set(input().split())

m_diff = m_set.difference(n_set)
m_diff.update(n_set.difference(m_set))

a = sorted(m_diff, key=int)
for e in a:
    print(e)
