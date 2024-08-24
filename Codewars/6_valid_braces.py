def valid_braces(string):
    braces = {
        'a': 0,
        'b': 0,
        'c': 0,
    }

    most_recent = []

    for ele in string:
        match ele:
            case '(':
                braces['a'] += 1
                most_recent.append('a')
            case '{':
                braces['b'] += 1
                most_recent.append('b')
            case '[':
                braces['c'] += 1
                most_recent.append('c')
            case ')':
                braces['a'] -= 1
                if braces.get('a') < 0 or most_recent.pop() != 'a': return False
            case '}':
                braces['b'] -= 1
                if braces.get('b') < 0 or most_recent.pop() != 'b': return False
            case ']':
                braces['c'] -= 1
                if braces.get('c') < 0 or most_recent.pop() != 'c': return False

    for key in braces:
        if braces[key] != 0: return False

    return True