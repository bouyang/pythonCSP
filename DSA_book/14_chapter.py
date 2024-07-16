class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self, first_node=None):
        self.first_node = first_node

    def read(self, index):
        current_node = self.first_node
        current_index = 0

        while current_index < index:
            current_node = current_node.next_node
            current_index += 1

            if not current_node:
                return None
            
        return current_node.data

    def search(self, value):
        current_node = self.first_node
        current_index = 0

        while current_node.data != value:
            current_node = current_node.next_node
            current_index += 1

            if not current_node:
                return None
        
        return current_index
    
    def insert(self, index, value):
        new_node = Node(value)

        if index == 0:
            new_node.next_node = self.first_node
            self.first_node = new_node
            return
        
        current_node = self.first_node
        current_index = 0

        while current_index < (index - 1):
            current_node = current_node.next_node
            current_index += 1

        new_node.next_node = current_node.next_node

        current_node.next_node = new_node

    def delete(self, index):
        if index == 0:
            self.first_node = self.first_node.next_node
            return
        
        current_node = self.first_node
        current_index = 0

        while current_index < (index - 1):
            current_node = current_node.next_node
            current_index += 1

        node_after_deleted_node = current_node.next_node.next_node

        current_node.next_node = node_after_deleted_node

    def print(self):
        current_node = self.first_node

        while current_node:
            print(current_node.data)
            current_node = current_node.next_node

    def last_value(self):
        current_node = self.first_node

        while current_node.next_node:
            current_node = current_node.next_node

        print(current_node.data)

    # def reverse_order(self):
    #     current_node = self.last_node

    #     while current_node:
    #         print(current_node.data)
    #         current_node = current_node.previous_node

    def reverse_list(self):
        current_node = self.first_node
        nodes = []

        while(current_node):
            nodes.append(current_node)
            current_node = current_node.next_node

        rev_nodes = nodes[::-1]

        for i in range(len(nodes) - 1):
            rev_nodes[i].next_node = rev_nodes[i + 1]

        rev_nodes[len(nodes) - 1].next_node = None

        self.first_node = rev_nodes[0]



node_1 = Node('once')
node_2 = Node('upon')
node_3 = Node('a')
node_4 = Node('time')

node_1.next_node = node_2
node_2.next_node = node_3
node_3.next_node = node_4

list = LinkedList(node_1)

# print(list.read(3))
# print(list.search('time'))

list.insert(2, 'purple')
# print(list.read(2))

list.delete(2)
# print(list.read(2))

list.print()

# list.last_value()
print('----')

list.reverse_list()
list.print()


def re_link(pointer):
    next_link = pointer.next_node
    pointer.next_node = next_link