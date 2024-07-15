def prob1(array):
    if not array:
        return 0
    return len(array[0]) + prob1(array[1:])

print(prob1(['ab', 'c', 'def', 'ghij']))



def prob2(array):
    if len(array) == 1:
        return array
    if (array[0] % 2 == 0):
        return [array[0]] + prob2(array[1:])
    else:
        return prob2(array[1:])
    
print(prob2([2, 3, 4, 5, 6]))



def prob3(n):
    if n == 1:
        return 1

    return n + prob3(n - 1)

print(prob3(7))



def prob4(str):

    if str[-1] == 'x':
        return len(str) - 1
    else:
        return prob4(str[:-1])

print(prob4('abcdefghijklmnopqrstuvwxyz'))



def prob5(rows, cols):
    if rows == 1 or cols == 1:
        return 1

    return prob5(rows, cols - 1) + prob5(rows - 1, cols)

def unique_paths(rows, columns):
    if rows == 1 or columns == 1:
        return 1
    return unique_paths(rows - 1, columns) + unique_paths(rows, columns - 1)

print(prob5(3, 7))
print(unique_paths(3, 7))