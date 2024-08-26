import re

def count_deaf_rats(town):
    town = re.sub(r'\s+', '', town)
    piper = False
    count = 0

    i = 0
    while i < len(town):
        print(town[i], piper)
        if town[i] == 'P':
            piper = True
            i -= 1
        elif town[i] == '~' and piper:
            count += 1
        elif town[i] == 'O' and (not piper):
            count += 1
        i += 2

    return count
        

# print(count_deaf_rats('~O~O~O~O P'))
print(count_deaf_rats("~O~O~O~O~O~O ~O~O~OO~~O~OO~~O~O ~O~O~O~O ~O~O~O~O~O~O~O~OO~~O ~O~O~O~O~O~O~O~O~O~O~O~O~OP"))