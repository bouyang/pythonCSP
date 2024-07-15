def accum(st):
    result = []
    for i in range(1, len(st) + 1):
        result.append((st[i - 1] * i).capitalize())
    return '-'.join(result)