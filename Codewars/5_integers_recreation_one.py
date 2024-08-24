import math

def list_squared(m, n):
    result = []
    for i in range(m, n + 1):
        divisors = find_divisors(i)
        sum_of_squares = sum([num ** 2 for num in divisors])
        if is_square(sum_of_squares):
            result.append([i, sum_of_squares])
    return result

def find_divisors(num):
    result = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            result.append(i)
            if num //i != i: result.append(num // i)
    return result

def is_square(num):
    return num // math.sqrt(num) == math.sqrt(num)


# print(is_square(84101))
# print(is_square(84100))
print(list_squared(1, 250))