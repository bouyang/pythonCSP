def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_factors(n):
    if is_prime(n): return f'({n})'

    result = ''
    i = 2
    while n > 1:
        if is_prime(n):
            result += f'({n})'
            n //= n
        elif is_prime(i):
            check = True
            counter = 0
            while check:
                if n % i == 0:
                    counter += 1
                    n //= i
                else:
                    check = False
            
            if counter == 1:
                result += f'({i})'
            elif counter > 1:
                result += f'({i}**{counter})'
        i += 1
    return result

print(prime_factors(86240))