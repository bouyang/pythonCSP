def maskify(cc):
    result = ''
    for i in range(len(cc)):
        if i < len(cc) - 4:
            result += '#'
        else:
            result += cc[i]
    return result