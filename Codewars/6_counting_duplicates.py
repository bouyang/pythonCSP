def duplicate_count(text):
    count = 0
    for letter in set(text.casefold()):
        if text.casefold().count(letter.casefold()) > 1:
            count += 1
    return count

print(duplicate_count('Indivisibilities'))