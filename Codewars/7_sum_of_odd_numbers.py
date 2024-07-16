def row_sum_odd_numbers(n):
    sum = 0
    current = 1
    for row in range(1, n + 1):
        for _ in range(row):
            if row == n:
                sum += current
            current += 2
    return sum

row_sum_odd_numbers(5)