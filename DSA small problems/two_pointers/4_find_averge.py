# def findAverages(nums, k):
#     result = []
#     for i in range(len(nums) - k + 1):
#         start = i
#         end = i + k - 1
#         sum = 0

#         while start <= end:
#             sum += nums[start]
#             start += 1

#         result.append(sum / k)

#     return result

def findAverages(nums, k):
    result = []
    sum = 0
    start = 0
    end = 0

    while end < len(nums):
        sum += nums[end]

        if end >= (k - 1):
            result.append(sum / k)
            sum -= nums[start]
            start += 1

        end += 1

    return result

print(findAverages([1, 2, 3, 4, 5, 6], 3)); # [ 2, 3, 4, 5 ]
print(findAverages([1, 2, 3, 4, 5], 2));    # [1.5, 2.5, 3.5, 4.5]
print(findAverages([10, 20, 30, 40, 50], 4)); # [ 25, 35 ]
print(findAverages([5, 5, 5, 5, 5], 1));      # [ 5, 5, 5, 5, 5 ]
print(findAverages([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)); # [2.2, 2.8, 2.4, 3.6, 2.8]