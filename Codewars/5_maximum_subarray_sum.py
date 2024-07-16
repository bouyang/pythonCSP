def max_sequence(arr):
    if not arr:
        return 0
    
    local_max = arr[0]
    global_max = arr[0]

    for i in range(1, len(arr)):
        local_max = max(local_max + arr[i], arr[i])
        global_max = max(global_max, local_max)

    if global_max >= 0:
        return global_max
    else:
        return 0


# print(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]))
print(max_sequence([3, -1, 5]))