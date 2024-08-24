def perimeter(n):
    if n == 0: return 1
    if n == 1: return 2

    result = 2

    first = 1
    second = 1

    for i in range(3, n + 2):
        sum = first + second
        result += sum
        first = second
        second = sum

    return 4 * result


print(perimeter(5))
# print(perimeter(7))