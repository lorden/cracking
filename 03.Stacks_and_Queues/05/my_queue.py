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
        if self.top is not None:
            return self.top.data
        return None


class MyQueue():
    newest = Stack()
    oldest = Stack()

    def shift_stacks(self):
        if self.oldest.peek() is None:
            while self.newest.peek() is not None:
                self.oldest.push(self.newest.pop().data)

    def enqueue(self, item):
        self.newest.push(item)

    def dequeue(self):
        self.shift_stacks()
        return self.oldest.pop()

    def peek(self):
        self.shift_stacks()
        return self.oldest.peek()


mq = MyQueue()
mq.enqueue(1)
print "Enqueue: 1"
mq.enqueue(2)
print "Enqueue: 2"
mq.enqueue(3)
print "Enqueue: 3"
mq.enqueue(4)
print "Enqueue: 4"
print "Peek: %s" % mq.peek()
mq.enqueue(5)
print "Enqueue: 5"
mq.enqueue(6)
print "Enqueue: 6"
print "Dequeued: %s" % mq.dequeue().data
print "Dequeued: %s" % mq.dequeue().data
print "Dequeued: %s" % mq.dequeue().data
print "Dequeued: %s" % mq.dequeue().data
mq.enqueue(7)
print "Enqueue: 7"
print "Peek: %s" % mq.peek()
print "Dequeued: %s" % mq.dequeue().data
print "Peek: %s" % mq.peek()
