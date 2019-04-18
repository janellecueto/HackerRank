# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for a in attrs:
            print("->",a[0],">",a[1])

parser = MyHTMLParser()
N = int(input())
for _ in range(N):
    parser.feed(input().strip())

