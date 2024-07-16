def printer_error(s):
    error = 0
    for letter in s:
        if letter in 'nopqrstuvwxyz':
            error += 1
    
    return f'{error}/{len(s)}'