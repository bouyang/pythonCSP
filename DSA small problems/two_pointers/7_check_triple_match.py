def checkTripleMatch(nums):
    result = {}

    for num in nums:
        if result.get(num):
            return True
        else:
            result[num * 3] = True
    
    return False


print(checkTripleMatch([1, 3, 9, 28]) == True)
print(checkTripleMatch([1, 2, 4, 10, 11, 12]) == True)
print(checkTripleMatch([0, 5, 7, 55]) == False)
print(checkTripleMatch([4, 5, 7, 9, 13, 15, 17]) == True)
print(checkTripleMatch([2, 6, 13, 54]) == True)
print(checkTripleMatch([1, 5, 17, 51]) == True)
print(checkTripleMatch([1, 2, 4, 8]) == False)