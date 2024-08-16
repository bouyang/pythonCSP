class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def createLinkedList(arr, cyclePos):
    head = Node(None)
    current = head
    cycleNode = None

    for i in range(len(arr)):
        current.next = Node(arr[i])
        current = current.next
        if i == cyclePos:
            cycleNode = current

    if cycleNode:
        current.next = cycleNode

    return head.next

def printLinkedList(head):
    current = head
    result = ''
    while current:
        result += str(current.data) + ' -> '
        current = current.next
    result += 'null'
    print(result)

def hasCycle(head):
    current = head
    seen = {}

    while current:
        if seen.get(current):
            return True
        else:
            seen[current] = True
        current = current.next

    return False

def hasCycle2(head):
    slow = head
    fast = head

    while slow and fast.next:
        fast = fast.next
        if fast and (fast == slow):
            return True
        else:
            slow = slow.next
            fast = fast.next

    return False



list1 = createLinkedList([3, 2, 0, -4], 1);
list2 = createLinkedList([1, 2], 0);
list3 = createLinkedList([1], -1);
list4 = createLinkedList([10, 20, 30, 40, 50, 60], 3);
list5 = createLinkedList([5, 15, 25, 35, 45], -1);

print(hasCycle(list1))
print(hasCycle(list2))
print(hasCycle(list3))
print(hasCycle(list4))
print(hasCycle(list5))

print(hasCycle2(list1))
print(hasCycle2(list2))
print(hasCycle2(list3))
print(hasCycle2(list4))
print(hasCycle2(list5))