def duplicate_encode(word):
    return ''.join(['(' if word.casefold().count(letter.casefold()) == 1
             else ')'
             for letter in word])