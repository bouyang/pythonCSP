def sort_array(source_array):
    odd = [num for num in source_array if num % 2 == 1]
    odd.sort(reverse = True)
    result = []

    for num in source_array:
        if num % 2 == 1:
            result.append(odd.pop())
        else:
            result.append(num)

    return result


print(sort_array([1, 3, 5, 2, 8, 4]))