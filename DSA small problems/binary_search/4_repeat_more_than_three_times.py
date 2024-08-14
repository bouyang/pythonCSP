def isTargetFrequent(nums, target):
    firstIndex = findFirstOccurrance(nums, target)
    lastIndex = findLastOccurrance(nums, target)

    if firstIndex == -1: return False

    return lastIndex - firstIndex >= 3

def findFirstOccurrance(nums, target):
    left = 0
    right = len(nums) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            result = mid
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return result

def findLastOccurrance(nums, target):
    left = 0
    right = len(nums) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            result = mid
            left = mid + 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return result




print(isTargetFrequent([1, 2, 3, 3, 3, 3, 4], 3) == True)
print(isTargetFrequent([1, 1, 1, 1, 2, 3, 4], 1) == True)
print(isTargetFrequent([1, 2, 3, 4, 5], 2) == False )
print(isTargetFrequent([1, 1, 3, 4, 5], 2) == False )
print(isTargetFrequent([2, 2, 2, 3, 3, 3, 4], 3) == False)
print(isTargetFrequent([4, 4, 4, 4, 4, 4, 4], 4) == True)