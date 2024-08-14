def findInNestedArray(matrix, target):
    left = 0
    right = len(matrix) - 1

    while left <= right:
        mid = (left + right) // 2
        current = matrix[mid]

        left2 = 0
        right2 = len(current) - 1

        if target < current[left2]:
            right = mid - 1
        elif target > current[right2]:
            left = mid + 1
        else:
            while left2 <= right2:
                mid2 = (left2 + right2) // 2
                if current[mid2] == target:
                    return True
                elif current[mid2] > target:
                    right2 = mid2 - 1
                else:
                    left2 = mid2 + 1
            return False
    return False


print(findInNestedArray([[4, 8, 12], [16, 20, 24], [28, 32, 36]], 20) == True)
print(findInNestedArray([[3, 6, 9], [12, 15, 18], [21, 24, 27]], 27) == True)
print(findInNestedArray([[1, 3, 5], [7, 9, 11], [13, 15, 17]], 19) == False)
print(findInNestedArray([[10, 20, 30], [40, 50, 60], [70, 80, 90]], 10) == True)
print(findInNestedArray([[15, 25, 35], [45, 55, 65], [75, 85, 95]], 5) == False)