def dir_reduc(arr):
    if not arr:
        return []
    
    opp = {
        'NORTH': 'SOUTH',
        'SOUTH': 'NORTH',
        'EAST': 'WEST',
        'WEST': 'EAST',
    }
    result = [arr[0]]

    for element in arr[1:]:
        if result and opp.get(result[-1]) == element:
            result.pop(-1)
        else:
            result.append(element)

    return result