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

def printLinkedList(head):
    current = head
    result = ''
    while current:
        result += str(current.data) + ' -> '
        current = current.next
    result += 'null'
    print(result)

def mergeSortedLists(list1, list2):
    dummyHead = Node(None)
    dummy = dummyHead
    current1 = list1
    current2 = list2

    while current1 or current2:
        if current1 and current2:
            if current1.data < current2.data:
                dummy.next = current1 
                current1 = current1.next
            else:
                dummy.next = current2
                current2 = current2.next
            dummy = dummy.next
        elif current1:
            dummy.next = current1
            dummy = dummy.next
            current1 = current1.next
        else:
            dummy.next = current2
            dummy = dummy.next
            current2 = current2.next

    return dummyHead.next

list1 = createLinkedList([1, 3, 5])
list2 = createLinkedList([2, 4, 6])
printLinkedList(mergeSortedLists(list1, list2))

list3 = createLinkedList([1, 2, 3]);
list4 = createLinkedList([]);
printLinkedList(mergeSortedLists(list3, list4))

list5 = createLinkedList([]);
list6 = createLinkedList([1]);
printLinkedList(mergeSortedLists(list5, list6))

list7 = createLinkedList([1, 5, 9]);
list8 = createLinkedList([2, 4, 6, 8, 10]);
printLinkedList(mergeSortedLists(list7, list8))

list9 = createLinkedList([1, 2, 5]);
list10 = createLinkedList([3, 6, 7]);
printLinkedList(mergeSortedLists(list9, list10))