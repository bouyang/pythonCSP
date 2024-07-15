def find_it(seq):
    result_count = {}
    for number in seq:
        if number not in result_count:
            result_count[number] = 0
        result_count[number] += 1

    print(result_count)
    
    for num, count in result_count.items():
        if count % 2 == 1:
            return num


print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))