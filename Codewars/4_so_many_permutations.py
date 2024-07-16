def permutations(s):
    if len(s) == 1:
        return s

    result = []
    right_side = permutations(s[1:])

    for element in right_side:
        for index in range(len(element) + 1):
            result.append(element[:index] + s[0] + element[index:])

    return set(result)

print(permutations('ab'))