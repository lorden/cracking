class Node:
    left = None
    right = None
    value = None

    def __init__(self, value):
        self.value = value


class Tree:
    root = None

    def insert_new(self, node, value):
        if node.value > value:
            if node.left:
                return self.insert_new(node.left, value)
            else:
                node.left = Node(value)
                return True
        if node.value < value:
            if node.right:
                return self.insert_new(node.right, value)
            else:
                node.right = Node(value)
                return True

    def insert(self, value):
        if not self.root:  # Tree is empty
            self.root = Node(value)
        else:
            self.insert_new(self.root, value)


def check_height(node):
    if not node:
        return 0
    left_height = check_height(node.left)
    if left_height == -1:
        return -1  # Not balanced
    right_height = check_height(node.right)
    if right_height == -1:
        return -1  # Not balanced

    if abs(left_height - right_height) > 1:
        return -1
    else:
        return max(left_height, right_height) + 1


def is_balanced(node):
    if check_height(node) == -1:
        return False
    else:
        return True

if __name__ == '__main__':
    t = Tree()
    t.insert(10)
    t.insert(5)
    t.insert(15)
    t.insert(3)
    t.insert(7)
    t.insert(12)
    t.insert(2)
    t.insert(1)

    print is_balanced(t.root)
