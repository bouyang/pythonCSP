def spin_words(sentence):
    result = []
    for word in sentence.split(' '):
        if len(word) < 5:
            result.append(word)
        else:
            result.append(word[::-1])
    return ' '.join(result)

print(spin_words('Stop Spinning My Words'))