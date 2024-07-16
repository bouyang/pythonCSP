from preloaded import MORSE_CODE

def decode_morse(morse_code):
    result = ''
    for code in morse_code.split(' '):
        result += MORSE_CODE.get(code, ' ')
    return result.strip().replace('  ', ' ')

decode_morse('... --- ...')
decode_morse('...   ---   ...')