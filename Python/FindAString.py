def count_substring(string, sub_string):
    return sum([1 for i in range(len(string) - len(sub_string) + 1) if string[i:i+len(sub_string)] == sub_string ])
#NOTE: list comprehension
#   this iterates through the entire string (less the length of the sub_string) and adds 1 to the sum list everytime 
#   a substring (string[i:i+len(sub_string)]) = sub_string

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
