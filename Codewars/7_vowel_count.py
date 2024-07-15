def get_count(sentence):
    return 0 + sentence.count('a') + sentence.count('e') + sentence.count('i') + sentence.count('o') + sentence.count('u')

print(get_count('hello world'))