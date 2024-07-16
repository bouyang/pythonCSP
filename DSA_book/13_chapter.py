class SortableArray:
    def __init__(self, array):
        self.array = array

    def partition(self, left_pointer, right_pointer):
        pivot_index = right_pointer
        pivot = self.array[pivot_index]

        right_pointer -= 1

        while True:

            while self.array[left_pointer] < pivot:
                left_pointer += 1

            while self.array[right_pointer] > pivot:
                right_pointer -= 1

            if left_pointer >= right_pointer:
                break
            else:
                self.array[left_pointer], self.array[right_pointer] = self.array[right_pointer], self.array[left_pointer]
                left_pointer += 1

        self.array[left_pointer], self.array[pivot_index] = self.array[pivot_index], self.array[left_pointer]

        return left_pointer
    
    def quicksort(self, left_index, right_index):
        if right_index - left_index <= 0:
            return
        pivot_index = self.partition(left_index, right_index)

        self.quicksort(left_index, pivot_index - 1)
        self.quicksort(pivot_index + 1, right_index)

    def quickselect(self, kth_lowest_value, left_index, right_index):
        if right_index - left_index <= 0:
            return self.array[left_index]
        
        pivot_index = self.partition(left_index, right_index)

        if kth_lowest_value < pivot_index:
            return self.quickselect(kth_lowest_value, left_index, pivot_index - 1)
        elif kth_lowest_value > pivot_index:
            return self.quickselect(kth_lowest_value, pivot_index + 1, right_index)
        else:
            return self.array[pivot_index]

array = [0, 50, 20, 10, 60, 30]
sortable_array = SortableArray(array)
# print(sortable_array.quickselect(1, 0, len(array) - 1))


def prob1(array):
    sortable_array = SortableArray(array)
    sortable_array.quicksort(0, len(array) - 1)
    return sortable_array.array[-1] * sortable_array.array[-2] * sortable_array.array[-3]

print(prob1([5, 2, 4, 1, 0]))

def prob2(array):
    sortable_array = SortableArray(array)
    sortable_array.quicksort(0, len(array) - 1)
    for i in range(len(array)):
        if sortable_array.array[i] != sortable_array.array[i + 1] - 1:
            return sortable_array.array[i] + 1
    return None

print(prob2([5, 2, 4, 1, 0]))

def prob3_1(array):
    result = array[0]

    for item in array:
        if item > result:
            result = item

    return result

def prob3_2(array):
    sortable_array = SortableArray(array)
    sortable_array.quicksort(0, len(array) - 1)

    return sortable_array.array[-1]

def prob3_3(array):
    for element in array:
        largest = True
        for element2 in array:
            if element < element2:
                largest = False
        if largest:
                return element

arr = [1, 5, 2, 8, 9, 10, 2, 4]
print(prob3_1(arr))
print(prob3_2(arr))
print(prob3_3(arr))