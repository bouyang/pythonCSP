def descending_order(num):
    return int(''.join(sorted(list(str(num)))[::-1]))

print(descending_order(1234346))