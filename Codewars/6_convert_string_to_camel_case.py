def to_camel_case(text):
    if text == '':
        return ''
    words = text.replace('-', ' ').replace('_', ' ').split()
    words2 = [word.capitalize() for word in words]
    return ''.join([words[0]] + words2[1:])

to_camel_case('the_stealth-warrior')