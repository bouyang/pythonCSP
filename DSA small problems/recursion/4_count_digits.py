def countDigits(nums):
    if nums // 10 == 0: return 1
    return 1 + countDigits(nums // 10)

print(countDigits(12345) == 5)
print(countDigits(7) == 1)
print(countDigits(100000) == 6)
print(countDigits(99999) == 5)
print(countDigits(0) == 1)