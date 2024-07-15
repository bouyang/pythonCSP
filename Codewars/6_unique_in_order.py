def unique_in_order(sequence):
    if not sequence:
        return []
    
    result = [list(sequence)[0]]

    for element in list(sequence)[1:]:
        if element != result[-1]:
            result.append(element)

    return result