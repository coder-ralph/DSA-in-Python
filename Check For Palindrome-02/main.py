s = input("Enter a string: ")

# function to check the palindrome

def palindrome(string):
    for i in range(1, int(len (string)/2)):
        if string[i] == string[len(string)-i-1]:
            return True
    return False


print(palindrome(s))