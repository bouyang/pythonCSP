# 1. 0
# 2. will go on past from 2 -> 0 -> -2 ...
# 3. if low > high, return

array = [1, 2, 3, [4, 5, 6], 7, [8, [9, 10, 11, [12, 13, 14]]], [15, 16, 17, 18, 19,[20, 21, 22, [23, 24, 25,[26, 27, 29]], 30, 31], 32, 33]]

def func(input):
    if type(input) is not list:
        print(input)
        return
    
    for element in input:
        func(element)

func(array)