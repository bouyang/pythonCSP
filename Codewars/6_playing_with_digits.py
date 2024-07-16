def dig_pow(n, p):
    digits = list(str(n))
    result = 0

    for exp in range(p, p + len(digits)):
        answer = 1
        for _ in range(exp):
            answer *= int(digits[exp - p])
        result += answer

    print(result)

    if result % n == 0:
        return result // n
    else:
        return -1

print(dig_pow(695, 2))
print(dig_pow(46288, 3))