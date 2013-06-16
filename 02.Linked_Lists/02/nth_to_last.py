from base import Node, print_nodes

def find_nth_to_last(root, nth):
    if root is None or nth < 0:
        return None
    p2 = root
    for x in xrange(0, nth):
        p2 = p2.next
        if p2 is None:
            return None
    p1 = root
    while p2.next is not None:
        p1 = p1.next
        p2 = p2.next
    return p1


root = Node(0)
root.append_to_tail(1)
root.append_to_tail(2)
root.append_to_tail(3)
root.append_to_tail(4)
root.append_to_tail(5)
root.append_to_tail(6)
root.append_to_tail(7)
root.append_to_tail(8)
root.append_to_tail(9)

print_nodes(root)
nth = 2
node = find_nth_to_last(root, nth)
print "%s to last: %s" % (nth, node.data)
