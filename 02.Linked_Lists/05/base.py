class Node:
    next = None
    data = 0

    def __init__(self, data):
        self.data = data

    def append_to_tail(self, data):
        end = Node(data)
        pointer = self
        while pointer.next is not None:
            pointer = pointer.next
        pointer.next = end


def delete_node(root, data):
    n = root
    if n.data == data:
        return n.next
    while n.next is not None:
        if n.next.data == data:
            n.next = n.next.next
            return root
        n = n.next


def print_nodes(root):
    nodes = [root.data]
    while root.next is not None:
        root = root.next
        nodes.append(root.data)
    print nodes

#root = Node(4)
#root.append_to_tail(5)
#root.append_to_tail(7)
#root.append_to_tail(8)
#root.append_to_tail(10)
#
#print_nodes(root)
#delete_node(root, 8)
#print_nodes(root)
