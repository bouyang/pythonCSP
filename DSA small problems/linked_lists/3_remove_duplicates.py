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

def deleteDuplicates(head):
    current = head

    while current:
        runner = current.next
        while runner and (runner.data == current.data):
            runner = runner.next
        current.next = runner
        current = runner

    return head

list1 = createLinkedList([1, 1, 2])
list2 = createLinkedList([1, 1, 2, 3, 3])
list3 = createLinkedList([1, 2, 3, 3, 4])
list4 = createLinkedList([2, 2, 2, 3, 3])
list5 = createLinkedList([5])

printLinkedList(deleteDuplicates(list1))
printLinkedList(deleteDuplicates(list2))
printLinkedList(deleteDuplicates(list3))
printLinkedList(deleteDuplicates(list4))
printLinkedList(deleteDuplicates(list5))