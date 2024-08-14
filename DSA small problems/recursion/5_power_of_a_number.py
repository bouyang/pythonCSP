def power(x, n):
    if n == 0: return 1
    return x * power(x, n - 1)

print(power(2, 3) == 8)
print(power(5, 0) == 1)
print(power(3, 4) == 81)
print(power(7, 2) == 49)
print(power(10, 1) == 10)