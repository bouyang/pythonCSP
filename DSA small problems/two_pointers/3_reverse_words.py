def reverseWords(str):
    result = []
    for word in str.split(' '):
        word = list(word)
        start = 0
        end = len(word) - 1

        while start < end:
            word[start], word[end] = word[end], word[start]
            start += 1
            end -= 1

        result.append(''.join(word))

    return (' ').join(result)

print(reverseWords("Hello World") == "olleH dlroW")
print(reverseWords("JavaScript is fun") == "tpircSavaJ si nuf")
print(reverseWords("Coding in the sun") == "gnidoC ni eht nus")
print(reverseWords("Launch School") == "hcnuaL loohcS")