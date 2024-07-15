def persistence(n):
    x = 0
    while n > 9:
        num_str = str(n)
        product = 1
        for i in range(0, len(num_str)):
            product *= int(num_str[i])
        n = product
        x += 1
    return x