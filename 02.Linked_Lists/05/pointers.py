from base import Node, print_nodes


def find_loop_start(node):
    n1 = node
    n2 = node

    while (n2.next is not None):
        n1 = n1.next
        n2 = n2.next.next
        if n1 is n2:
            break

    if n2.next is None:
        return None

    n1 = node
    while n1 is not n2:
        n1 = n1.next
        n2 = n2.next

    return n2

root = Node('A')
root.append_to_tail('B')
root.append_to_tail('C')
root.append_to_tail('D')
root.append_to_tail('E')
root.next.next.next.next.next = root.next.next

loop_start = find_loop_start(root)
print loop_start.data
