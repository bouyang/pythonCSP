def tribonacci(signature, n):
    if n == 0:
        return []
    elif n == 1:
        return [signature[0]]
    elif n == 2:
        return [signature[0], signature[1]]
    elif n == 3:
        return signature
    
    first = signature[0]
    second = signature[1]
    third = signature[2]

    result = signature
    
    for _ in range(n - 3):
        sum = first + second + third
        result.append(sum)
        first = second
        second = third
        third = sum

    return result