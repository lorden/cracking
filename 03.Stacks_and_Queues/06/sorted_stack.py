class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data

    def append(self, data):
        node = self
        while node.next is not None:
            node = node.next
        node.next = Node(data)


class Stack:
    top = None

    def push(self, item):
        node = Node(item)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is not None:
            node = self.top
            self.top = self.top.next
            return node.data
        return None

    def print_stack(self):
        nodes = ['TOP']
        node = self.top
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('BOTTOM')
        print nodes

    def peek(self):
        if self.top is not None:
            return self.top.data
        return None

    def is_empty(self):
        return self.top is None


def sort_stack(stack):
    aux = Stack()
    while not stack.is_empty():
        tmp = stack.pop()
        while not aux.is_empty() and aux.peek() > tmp:
            stack.push(aux.pop())
        aux.push(tmp)
    return aux


stack = Stack()
stack.push(6)
stack.push(2)
stack.push(4)
stack.push(1)
stack.push(5)
stack.push(3)
stack = sort_stack(stack)
stack.print_stack()
