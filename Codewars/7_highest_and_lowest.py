def high_and_low(numbers):
    numbers = [int(num) for num in numbers.split(' ')]
    return f'{max(numbers)} {min(numbers)}'

print(high_and_low('8 3 -5 42 -9 0'))