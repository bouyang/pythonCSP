def find_outlier(integers):
    count = 0
    for i in range(0, 3):
        if integers[i] % 2 == 0:
            count += 1
    
    if count >= 2:
        for i in range(0, len(integers)):
            if integers[i] % 2 == 1:
                return integers[i]
    else:
        for i in range(0, len(integers)):
            if integers[i] % 2 == 0:
                return integers[i]