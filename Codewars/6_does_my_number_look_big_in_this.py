def narcissistic(value):
    digits = len(str(value))
    sum = 0

    for digit in str(value):
        sum += int(digit)**digits

    return sum == value