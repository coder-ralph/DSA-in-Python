# reversing a given number

def rev_num(num):
    rev = 0
    while num > 0:
        reminder = num % 10
        rev = (rev * 10) + reminder
        num = num // 10
    return rev

print(f"reverse of the given number is {rev_num(int(input('Enter a number: ')))}")

# you cam also use this way
# print(f"reverse of the given number is {rev_num(123456789)}")