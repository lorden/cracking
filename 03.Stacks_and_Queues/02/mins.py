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
            return node
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
        return self.top.data


class StackWithMins(Stack):
    mins = Stack()

    def push(self, item):
        node = Node(item)
        node.next = self.top
        self.top = node
        if self.mins.top is not None:
            if self.mins.top.data > item:
                self.mins.push(item)
        else:
            self.mins.push(item)

    def pop(self):
        if self.top is not None:
            if self.peek() == self.mins.peek():
                self.mins.pop()
            node = self.top
            self.top = self.top.next
            return node
        return None

    def min(self):
        return self.mins.peek()


stack = StackWithMins()
stack.push(9)
stack.push(5)
stack.push(7)
stack.push(4)
stack.push(3)
stack.push(6)
stack.push(5)
stack.push(2)
stack.push(1)
stack.print_stack()
stack.mins.print_stack()
stack.pop()
stack.pop()
print stack.min()
stack.print_stack()
