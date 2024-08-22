def delete_nth(order, max_e):
    seen = {}
    result = []

    for item in order:
        if  seen.get(item) == None or seen.get(item) < max_e:
            seen[item] = seen.get(item, 0) + 1
            result.append(item)

    return result


print(delete_nth([1,2,3,1,2,1,2,3], 2))