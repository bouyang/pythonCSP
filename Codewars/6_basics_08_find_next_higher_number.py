def next_higher(n):
    binary_num = '0' + bin(n)[2:]
    index = binary_num.rfind('01')
    result = binary_num[:index] + '10' + ''.join(sorted(binary_num[index + 2:]))

    return int(result, 2)

    i = s.rfind('01')
    s = s[:i] + '10' + ''.join(sorted(s[i+2:]))
    return int(s, 2)

print(next_higher(1022))

print()
print()

print(list(bin(1022)[2:]))
print(list(bin(1279)[2:]))

print(1279 - 1022)