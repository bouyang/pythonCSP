def score(dice):
    current = list(dice)
    score = 0
    scoring = {
        1: 1000,
        6: 600,
        5: 500,
        4: 400,
        3: 300,
        2: 200
    }

    for i in range(1, 7):
        if current.count(i) >= 3:
            score += scoring.get(i)
            current.remove(i)
            current.remove(i)
            current.remove(i)

    score += current.count(1) * 100
    score += current.count(5) * 50

    return score
            


print(score([5, 1, 3, 4, 1]))
print(score([1, 1, 1, 3, 1]))
print(score([4, 4, 4, 3, 3]))