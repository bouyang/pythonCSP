def is_square(n):
    if n < 0: return False
    for i in range(0, n // 2 + 1):
        if i**2 == n: return True
        if i**2 > n: return False
    return False