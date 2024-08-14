def reverseConsonants(str):
    VOWELS = 'aeiouAEIOU'
    result = list(str)
    start = 0
    end = len(str) - 1

    while start < end:
        if str[start] in VOWELS:
            result[start] = str[start]
            start += 1
        elif str[end] in VOWELS:
            result[end] = str[end]
            end -= 1
        else:
            result[start], result[end] = str[end], str[start]
            start += 1
            end -= 1

    return ''.join(result)


print(reverseConsonants("") == "")
print(reverseConsonants("s") == "s")
print(reverseConsonants("hello") == "lelho")
print(reverseConsonants("leetcode") == "deectole")
print(reverseConsonants("example") == "elapmxe")
print(reverseConsonants("Consonants") == "sotnonasnC")