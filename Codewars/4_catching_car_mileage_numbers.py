def is_interesting(number, awesome_phrases):
    if number < 98:
        return 0
    
    if number != 98 and number != 99:
        if zeroes(number) or same_num(number) or sequential_up(number) or sequential_down(number) or palindrome(number) or awesome(number, awesome_phrases):
            return 2
    
    for i in range(1, 3):
        if zeroes(number + i) or same_num(number + i) or sequential_up(number + i) or sequential_down(number + i) or palindrome(number + i) or awesome(number + i, awesome_phrases):
            return 1
        
    return 0
    
def zeroes(number):
    return str(number).count('0') == len(str(number)) - 1

def same_num(number):
    return str(number).count(str(number)[0]) == len(str(number))

def sequential_up(number):    
    digits = list(str(number))

    for index, digit in enumerate(digits[1:]):
        if digit == '0':
            digit = '10'

        if int(digit) != int(digits[index]) + 1:
            return False

    return True

def sequential_down(number):    
    digits = list(str(number))
    for index, digit in enumerate(digits[1:]):    
        if int(digit) != int(digits[index]) - 1:
            return False

    return True

def palindrome(number):
    digits = list(str(number))
    return list(reversed(digits)) == digits

def awesome(number, array):
    if not array:
        return False
    return number in array

print(is_interesting(99, [1337, 256]))
print(is_interesting(3210, [1337, 256]))