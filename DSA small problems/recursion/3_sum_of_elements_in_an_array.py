def sum(nums):
    if len(nums) == 0: return 0
    return nums[0] + sum(nums[1:])

print(sum([1,2,3]) == 6)
print(sum([10, 15, 20, 10, 5]) == 60)
print(sum([-5, -1, 5, 2, -3]) == -2)
print(sum([7]) == 7)
print(sum([]) == 0)