# def anagram(digits):
#     if len(digits) == 1:
#         return digits

#     result = []
#     subarr = anagram(digits[1:])
#     for element in subarr:
#         for index in range(len(element) + 1):
#             new_item = element[:index] + digits[0] + element[index:]
#             result.append(new_item)
    
#     return set(result)

# def next_bigger(n):
#     digits = list(str(n))
#     anagrams = anagram(digits)
#     anagrams = sorted([int(num) for num in anagrams])

#     index = anagrams.index(n)
    
#     if index == len(anagrams) - 1:
#         return -1
#     else:
#         return anagrams[index + 1]

def next_bigger(n):
    digits = list(str(n))
    sorted_digits = sorted(digits)
    current = n

    if list(reversed(sorted_digits)) == digits:
        return -1

    while True:
        current += 1
        if sorted(list(str(current))) == sorted_digits:
            return current

print(next_bigger(21))

print(414 - 144)
print((bin(414))[2:])
print((bin(144))[2:])
