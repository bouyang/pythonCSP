def countPairs(nums, target):
    result = 0
    start = 0

    while start < len(nums) - 1:
        end = start + 1
        while end < len(nums):
            if nums[start] + nums[end] > target:
                result += 1
            end += 1
        start += 1
        
    return result


print(countPairs([1, 2, 3, 4, 5], 6) == 4)

print(countPairs([1, 2, 3, 4, 5], 8) == 1)

print(countPairs([1, 3, 5, 7], 6) == 4)

print(countPairs([1, 2, 3, 4], 5) == 2)

print(countPairs([1, 2, 3, 4, 5], 10) == 0)