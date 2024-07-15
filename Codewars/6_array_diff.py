def array_diff(a, b):
    return [number for number in a if number not in b]

print (array_diff([1, 2, 2], [1]))