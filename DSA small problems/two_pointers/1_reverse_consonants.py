CONS = 'bcdfghjklmnpqrstvwxyz'

def reverse_consonants(str):
    if not str:
        return ''
    
    str = list(str)
    lp = 0
    rp = len(str) - 1

    while lp < rp:
        if str[lp].casefold() in CONS and str[rp].casefold() in CONS:
            temp = str[lp]
            str[lp] = str[rp]
            str[rp] = temp
            lp += 1
            rp -= 1
        elif str[lp].casefold() in CONS:
            rp -= 1
        elif str[rp].casefold() in CONS:
            lp += 1
        else:
            lp += 1
            rp -= 1

    return ''.join(str)


print(reverse_consonants('Consonants'))