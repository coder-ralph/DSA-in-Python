# check for palindrome

s = input("Enter a string: ")

# reverse a given string
def palindrome(string):
    x = ""
    for i in string:
        x = i + x
    return x

if s == palindrome(s):
    print("It is a Palindrome")
else :
    print("It is not a Palindrome")