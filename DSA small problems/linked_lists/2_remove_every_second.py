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

def removeEverySecondNode(head):
    current = head
    previous = None
    remove = False
    while current:
        if remove:
            previous.next = current.next
            remove = False
        else:
            previous = current
            remove = True
        current = current.next
    return head

list1 = createLinkedList([1, 2, 3, 4, 5]);
list2 = createLinkedList([1, 2]);
list3 = createLinkedList([1]);
list4 = createLinkedList([1, 2, 3, 4]);
list5 = createLinkedList([]);

printLinkedList(removeEverySecondNode(list1))
printLinkedList(removeEverySecondNode(list2))
printLinkedList(removeEverySecondNode(list3))
printLinkedList(removeEverySecondNode(list4))
printLinkedList(removeEverySecondNode(list5))