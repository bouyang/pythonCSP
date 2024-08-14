def isSquareInteger(num):
    nums = list(range(1, num + 1))
    
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if num == nums[mid] ** 2:
            return True
        elif num > nums[mid] ** 2:
            left = mid + 1
        else:
            right = mid - 1

    return False

print(isSquareInteger(1) == True)
print(isSquareInteger(4) == True)
print(isSquareInteger(16) == True)
print(isSquareInteger(14) == False)
print(isSquareInteger(25) == True)
print(isSquareInteger(26) == False)