def order(sentence):
    result = ['', '', '', '', '', '', '', '', '']
    for word in sentence.split():
        for num in '123456789':
            if word.count(num) >= 1:
                result[int(num) - 1] = word
    
    return ' '.join(result).strip()

order('is2 Thi1s T4est 3a')