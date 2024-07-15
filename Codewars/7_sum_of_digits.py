def digital_root(n):
    result = n
    while len(str(n)) > 1:
        result = 0
        for digit in list(str(n)):
            result += int(digit)
        n = result
    return result

print(digital_root(942))