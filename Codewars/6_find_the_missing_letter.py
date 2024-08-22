import string

def find_missing_letter(chars):
    letters = string.ascii_lowercase + string.ascii_uppercase
    index = letters.find(chars[0])

    for i in range(len(chars)):
        if letters[index + i] != chars[i]:
            return letters[index + i]

print(find_missing_letter(['a', 'b', 'c', 'd', 'f']))