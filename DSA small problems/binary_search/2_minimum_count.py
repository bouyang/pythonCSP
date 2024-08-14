def minimumCount(nums):
    if len(nums) == 0: return 0

    left = 0
    right = len(nums) - 1
    firstPos = 0

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < 0:
            left = mid + 1
        elif nums[mid] > 0:
            firstPos = mid
            right = mid - 1
        else:
            return min(mid, len(nums) - mid - 1)

    return min(firstPos, len(nums) - firstPos)

print(minimumCount([-4, -3, -2, -1, 3, 4]) == 2)
print(minimumCount([-3, 1, 2, 3, 4, 5]) == 1)
print(minimumCount([-5, -4, -3, -2, -1]) == 0)
print(minimumCount([1, 2, 3, 4, 5]) == 0)
print(minimumCount([-2, -1, 1, 2]) == 2)
print(minimumCount([-7, -5, -4, 1, 2, 6, 10]) == 3)
print(minimumCount([-3, -2, -1, 0, 5, 6]) == 2)
print(minimumCount([-1, 0, 1]) == 1)
print(minimumCount([]) == 0)