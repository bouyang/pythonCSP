def findLargestIndex(nums):
    left = 0
    right = len(nums) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == mid:
            result = mid
            left = mid + 1
        elif nums[mid] > mid:
            right = mid - 1
        else:
            left = mid + 1
    return result


print(findLargestIndex([-1, 0, 2, 3]) == 3)
print(findLargestIndex([0, 1, 2, 3, 4]) == 4)
print(findLargestIndex([-5, 0, 3, 4, 7, 9]) == -1)
print(findLargestIndex([-2, 0, 1, 3, 3, 5]) == 5)
print(findLargestIndex([0]) == 0)