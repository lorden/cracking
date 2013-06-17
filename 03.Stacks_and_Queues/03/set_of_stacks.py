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


class SetOfStacks():
    threshold = 5
    top = None
    num_of_stacks = 0

    def push(self, item):
        if self.top is None:
            self.top = Node(Stack())
            self.top.data.push(item)
            self.threshold -= 1
            self.num_of_stacks += 1
        else:
            if self.threshold > 0:
                self.top.data.push(item)
                self.threshold -= 1
            else:
                stack = Node(Stack())
                stack.data.top = Node(item)
                stack.next = self.top
                self.top = stack
                self.threshold = 4
                self.num_of_stacks += 1

    def pop(self):
        node = self.top.data.pop()
        if self.top.data.top is None:
            self.top = self.top.next
            self.num_of_stacks -= 1
        return node

    def pop_at(self, index):  # allows partially filled stacks
        if index < 0:
            return None
        stack = self.top
        while index + 1 < self.num_of_stacks:
            stack = stack.next
            index += 1
        return stack.data.pop()

    def print_stack(self):
        set_of_nodes = []
        node = self.top
        while node is not None:
            stack = node.data.top
            nodes = []
            while stack is not None:
                nodes.append(stack.data)
                stack = stack.next
            set_of_nodes.append(nodes)
            node = node.next
        print set_of_nodes


stack = SetOfStacks()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)
stack.push(9)
stack.push(10)
stack.push(11)
stack.push(12)
#stack.pop()
#stack.pop()
#stack.pop()
print "Popped: %s" % stack.pop_at(0)
stack.print_stack()
