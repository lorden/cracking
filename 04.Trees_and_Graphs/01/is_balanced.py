class Node:
    left = None
    right = None
    value = None

    def __init__(self, value):
        self.value = value


def get_height(node):
    if not node:
        return 0
    return max(get_height(node.left), get_height(node.right)) + 1


def is_balanced(node):
    if not node:
        return True
    if abs(get_height(node.left) - get_height(node.right)) > 1:
        return False
    else:
        return is_balanced(node.left) and is_balanced(node.right)


if __name__ == '__main__':
    root = Node('A')
    root.left = Node('B')
    root.right = Node('C')
    root.left.left = Node('D')
    root.left.right = Node('E')
    root.right.left = Node('F')
    # Balanced until here
    root.right.left.left = Node('G')
    root.right.left.left.left = Node('H')

    print is_balanced(root)
