def reverseString(str):
    if len(str) <= 1: return str
    return reverseString(str[1:]) + str[0]

print(reverseString("hello") == "olleh")
print(reverseString("world") == "dlrow")
print(reverseString("a") == "a")
print(reverseString("") == "")
print(reverseString("recursion") == "noisrucer")