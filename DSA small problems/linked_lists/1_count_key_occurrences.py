class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def createLinkedList(arr):
    head = Node(None)
    current = head
    for val in arr:
        current.next = Node(val)
        current = current.next

    return head.next

list1 = createLinkedList([1, 2, 1, 2, 1, 3, 1]);
list2 = createLinkedList([4, 4, 4, 4]);
list3 = createLinkedList([1, 2, 3, 4, 5]);
list4 = createLinkedList([5, 5, 1, 2, 3, 5, 5]);
list5 = createLinkedList([]);
list6 = createLinkedList([1, 2, 3, 1, 1]);

def countKeyOccurrences(list, key):
    current = list
    count = 0
    while current:
        if current.data == key:
            count += 1
        current = current.next
    return count


print(countKeyOccurrences(list1, 1) == 4)
print(countKeyOccurrences(list2, 4) == 4)
print(countKeyOccurrences(list3, 1) == 1)
print(countKeyOccurrences(list4, 5) == 4)
print(countKeyOccurrences(list5, 1) == 0)
print(countKeyOccurrences(list6, 1) == 3)