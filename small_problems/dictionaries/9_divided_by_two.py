numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}

half_numbers = []

for number in numbers:
    half_numbers.append(numbers[number] // 2)

print(half_numbers)