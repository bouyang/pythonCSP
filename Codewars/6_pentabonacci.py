def count_odd_pentaFib(n):
    return pentafib(n, {})[1]

def pentafib(n, memo):
    match n:
        case 0:
            return [0, 1]
        case 1:
            return [1, 1]
        case 2:
            return [1, 1]
        case 3:
            return [2, 1]
        case 4:
            return [4, 1]
    
    if memo.get(n):
        return memo.get(n)
    else:
        new_num = (pentafib(n - 1, memo)[0] + pentafib(n - 2, memo)[0] + pentafib(n - 3, memo)[0] + pentafib(n - 4, memo)[0] + pentafib(n - 5, memo)[0])
        num_odds = pentafib(n - 1, memo)[1]

        if new_num % 2 == 1:
            memo[n] = [new_num, num_odds + 1]
            return [new_num, num_odds + 1]
        else:
            memo[n] = [new_num, num_odds]
            return [new_num, num_odds]


# print(pentafib(5, {}))
# print(pentafib(45, {}))
# print(pentafib(7, {}))

# print(count_odd_pentaFib(5))
# print('----')
# print(count_odd_pentaFib(10))

print(count_odd_pentaFib(15))


# 0, 1, 1, 2, 4, 8, 15, 