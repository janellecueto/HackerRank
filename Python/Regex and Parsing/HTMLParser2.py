from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if len(data.split('\n')) > 1:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        if data.strip():
            print(data)
    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)

html = ""       
for i in range(int(input())):
    html += input().strip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
