# reverse a string

s = input("Enter a string: ")

# reverse a given string
def palindrome(string):
    x = ""
    for i in string:
        x = i + x
    return x

print(palindrome(s))