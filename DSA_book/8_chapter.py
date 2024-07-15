def intersection(arr1, arr2):
    arr1_hash = {}
    result = []

    for element in arr1:
        arr1_hash[element] = True
    
    for element in arr2:
        if arr1_hash.get(element):
            result.append(element)
    
    return result

print(intersection([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 2, 4, 6, 8]))

def duplicate(array):
    hsh = {}
    for letter in array:
        if hsh.get(letter):
            return letter
        else:
            hsh[letter] = True

print(duplicate(['a', 'b', 'c', 'd', 'c', 'e']))

def missing(str):
    hsh = {}
    for letter in str:
        if letter:
            hsh[letter] = True
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if not hsh.get(letter):
            return letter
        
print(missing('the quick brown box jumps over a lazy dog'))

def nondup(str):
    hsh = {}
    for letter in str:
        if not hsh.get(letter):
            hsh[letter] = 1
        else:
            hsh[letter] += 1
    for letter in str:
        if hsh.get(letter) == 1:
            return letter

print(nondup('minimum'))