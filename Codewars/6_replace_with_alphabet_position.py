def alphabet_position(text):
    return ' '.join([str('abcdefghijklmnopqrstuvwxyz'.index(letter.casefold()) + 1) for letter in text if letter.casefold() in 'abcdefghijklmnopqrstuvwxyz'])