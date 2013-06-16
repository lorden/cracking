from base import Node, print_nodes

def remove_duplicates(root):
    n = root
    prev = None
    d = {}
    while n is not None:
        if n.data in d:
            prev.next = n.next
        else:
            d[n.data] = 1
            prev = n
        n = n.next

root = Node(4)
root.append_to_tail(5)
root.append_to_tail(8)
root.append_to_tail(7)
root.append_to_tail(8)
root.append_to_tail(10)
root.append_to_tail(8)
root.append_to_tail(10)

print_nodes(root)
remove_duplicates(root)
print_nodes(root)
