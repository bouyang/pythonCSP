def prob1(arr1, arr2):
    basketball_hash = {}
    result = []
    for player in arr1:
        name = f'{player['first_name']} {player['last_name']}'
        if name not in basketball_hash:
            basketball_hash[name] = True
    
    for player in arr2:
        name = f'{player['first_name']} {player['last_name']}'
        if name in basketball_hash:
            result.append(name)

    return result
    

basketball_players = [  {'first_name': "Jill", 'last_name': "Huang", 'team': "Gators"},  {'first_name': "Janko", 'last_name': "Barton", 'team': "Sharks"},  {'first_name': "Wanda", 'last_name': "Vakulskas", 'team': "Sharks"},  {'first_name': "Jill", 'last_name': "Moloney", 'team': "Gators"},  {'first_name': "Luuk", 'last_name': "Watkins", 'team': "Gators"}]
football_players = [  {'first_name': "Hanzla", 'last_name': "Radosti", 'team': "32ers"},  {'first_name': "Tina", 'last_name': "Watkins", 'team': "Barleycorns"}, {'first_name': "Alex", 'last_name': "Patel", 'team': "32ers"},  {'first_name': "Jill", 'last_name': "Huang", 'team': "Barleycorns"}, {'first_name': "Wanda", 'last_name': "Vakulskas", 'team': "Barleycorns"}]

# print(prob1(basketball_players, football_players))



def prob2(arr):
    max_num = max(arr)
    max_sum = sum(range(max_num + 1))
    return max_sum - sum(arr)

# print(prob2([8, 2, 3, 9, 4, 7, 5, 0, 6]))


def prob3(arr):
    profit = 0
    buy = arr[0]

    for ele in arr:
        if ele - buy > profit:
            profit = ele - buy
        elif ele < buy:
            buy = ele

    return profit

# print(prob3([10, 7, 5, 8, 11, 2, 6]))


def prob4(arr):
    highest_positive = [0, 0]
    highest_negative = [0, 0]
    
    for num in arr:
        if num > 0:
            if num > min(highest_positive):
                highest_positive = [max(highest_positive), num]
        if num < 0:
            if num < max(highest_negative):
                highest_negative = [min(highest_negative), num]

    return max(highest_positive[0] * highest_positive[1], highest_negative[0] * highest_negative[1])


# print(prob4([5, -10, -6, 9, 4]))

def prob5(arr):
    result = []

    while len(arr) > 1:
        minimum = min(arr)
        result.append(minimum)
        arr.remove(minimum)

    return result

# print(prob5([98, 99, 95, 105, 104, 98, 101, 99, 100, 97]))


def prob6(arr):
    length = 0
    next_num = {}

    for ele in arr:
        if (ele + 1) in arr:
            next_num[ele] = True
    
    for ele in arr:
        for i in range(len(arr)):
            if not next_num.get(ele + i):
                if i > length:
                    length = i
                break

    return length + 1

print(prob6([10, 5, 12, 3, 55, 30, 4, 11, 2]))
print(prob6([19, 13, 15, 12, 18, 14, 17, 11]))