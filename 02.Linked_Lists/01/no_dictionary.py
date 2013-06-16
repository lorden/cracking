from base import Node, print_nodes


def remove_duplicates(root):
    if root is None:
        return
    previous = root
    current = previous.next
    while current is not None:
        runner = root
        while runner is not current:
            if runner.data == current.data:
                tmp = current.next
                previous.next = tmp
                current = tmp
                break
            runner = runner.next
        if runner is current and runner is not None:
            previous = current
            current = current.next


root = Node(4)
root.append_to_tail(4)
root.append_to_tail(4)
root.append_to_tail(5)
root.append_to_tail(8)
root.append_to_tail(7)
root.append_to_tail(8)
root.append_to_tail(9)
root.append_to_tail(9)
root.append_to_tail(9)
root.append_to_tail(10)
root.append_to_tail(8)
root.append_to_tail(10)

print_nodes(root)
remove_duplicates(root)
print_nodes(root)
