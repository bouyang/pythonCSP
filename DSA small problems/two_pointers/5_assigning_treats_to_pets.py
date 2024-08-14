def assignTreats(appetite, treats):
    appetite.sort()
    treats.sort()
    count = 0

    p1 = 0
    p2 = 0

    while p2 < len(treats) and p1 < len(appetite):
        if treats[p2] >= appetite[p1]:
            count += 1
            p1 += 1
        p2 += 1

    return count

print(assignTreats([3, 4, 2], [1, 2, 3]) == 2)
print(assignTreats([1, 5], [5, 5, 6]) == 2)
print(assignTreats([1, 2, 3], [3]) == 1)
print(assignTreats([2], [1, 2, 1, 1]) == 1)
print(assignTreats([4, 3, 1], [2, 1, 3]) == 2)
print(assignTreats([1,2,3], [1,2,3]) == 3)
print(assignTreats([4, 5, 6], [1,2,3]) == 0)