def reduceToUnique(nums):
    p1 = 0
    p2 = 1

    while p2 < len(nums):
        if nums[p1] == nums[p2]:
            del nums[p2]
        else:
            p1 += 1
            p2 = p1 + 1
    
    return nums

print(reduceToUnique([3, 3, 5, 7, 7, 8]))
print(reduceToUnique([1, 1, 2, 2, 2, 3, 4, 4, 5]))
print(reduceToUnique([0]))
print(reduceToUnique([-5, -3, -3, -1, 0, 0, 0, 1]))
print(reduceToUnique([6, 6, 6, 6, 6, 6, 6]))