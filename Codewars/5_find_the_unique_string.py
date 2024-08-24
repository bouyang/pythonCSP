def find_uniq(arr):
    chars = []
    for ele in arr:
        chars.append(''.join(sorted((list(set(''.join(letter.casefold() for letter in list(ele))))))).strip())

    seen = {}
    uniq_idx = 0

    for idx, char in enumerate(chars):
        if char in seen:
            seen[char] += 1
            if chars[uniq_idx] == char:
                uniq_idx = prev_idx
        else:
            prev_idx = uniq_idx
            uniq_idx = idx
            seen[char] = 1

    return arr[uniq_idx]

print(find_uniq(['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a']))
print(find_uniq(['foobar', 'barfo', 'fobara', '   ', 'fobra', 'oooofrab']))
print(find_uniq(['    ', '  ', ' ', 'a', ' ', '']))