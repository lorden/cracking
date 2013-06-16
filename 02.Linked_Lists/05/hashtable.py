from base import Node, print_nodes


def find_loop_start(node):
    nodes = {}
    while node is not None:
        if node not in nodes:
            nodes[node] = 1
        else:
            return node
        node = node.next

root = Node('A')
root.append_to_tail('B')
root.append_to_tail('C')
root.append_to_tail('D')
root.append_to_tail('E')
root.next.next.next.next.next = root.next.next

loop_start = find_loop_start(root)
print loop_start.data
