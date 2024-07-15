def add_until_100(array):
    if not array:
        return 0
    
    current = add_until_100(array[1:])
    
    if array[0] + current > 100:
        return current
    else:
        return array[0] + current
    
print(add_until_100([12, 325, 123, 35, 2, 62, 4, 23]))



def golomb(n, mem):
    if n == 1:
        return 1
    
    if mem.get(n):
        return mem.get(n)
    else:
        result = 1 + golomb((n - golomb((golomb((n - 1), mem)), mem)), mem)
        mem[n] = result
        return result



def unique_paths(rows, columns, mem):
    if rows == 1 or columns == 1:
        return 1
    
    if mem.get((rows, columns)):
        return mem.get((rows, columns))
    else:
        result = unique_paths(rows - 1, columns, mem) + unique_paths(rows, columns - 1, mem)
        mem[(rows, columns)] = result
        return result

print(unique_paths(3, 7, {}))