# class Queue:
#     def __init__(self):
#         self.data = []

#     def enqueue(self, element):
#         self.data.append(element)

#     def dequeue(self):
#         if len(self.data) > 0:
#             return self.data.pop(0)
#         else:
#             return None
        
#     def read(self):
#         if len(self.data) > 0:
#             return self.data[0]
#         else:
#             return None

# 1. queue
# 2. 4
# 3. 3

class Stack:
    def __init__(self):
            self.data = []
            
    def push(self, element):
            self.data.append(element)
            
    def pop(self):
            if len(self.data) > 0:
                    return self.data.pop()
            else:
                    return None
                    
    def read(self):
            if len(self.data) > 0:
                    return self.data[-1]
            else:
                    return None
            
stack = Stack()

def reverse_str(str):
    stack = Stack()
    result = []

    for letter in str:
        stack.push(letter)
    
    while stack.read():
        result.append(stack.pop())

    return ''.join(result)

print(reverse_str('abcdef'))