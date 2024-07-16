def move_zeros(lst):
    zeroes = []
    other = []
    for ele in lst:
        if ele == 0:
            zeroes.append(0)
        else:
            other.append(ele)
    return other + zeroes
    