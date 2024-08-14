def sumOfNaturalNumbers(n):
    if n == 0: return 0
    return n + sumOfNaturalNumbers(n - 1)

print(sumOfNaturalNumbers(1) == 1)
print(sumOfNaturalNumbers(5) == 15)
print(sumOfNaturalNumbers(10) == 55)
print(sumOfNaturalNumbers(20) == 210)
print(sumOfNaturalNumbers(0) == 0)