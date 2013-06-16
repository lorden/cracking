from base import Node, print_nodes


def delete_node_without_root(node):
    if node is not None and node.next is not None:
        node.data = node.next.data
        node.next = node.next.next


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
node = root.next.next.next
delete_node_without_root(node)
print_nodes(root)
