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


def insert_from_array(tree, array):
    if len(array) > 1:
        middle = int(round(len(array) / 2))
        tree.insert(array[middle])
        insert_from_array(tree, array[0:middle])
        insert_from_array(tree, array[middle + 1:])
    elif array:
        tree.insert(array[0])
    return

if __name__ == '__main__':
    bst = Tree()
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    insert_from_array(bst, array)
    print bst.root.value  # 5

    print bst.root.left.value  # 2
    print bst.root.right.value  # 8

    print bst.root.left.left.value  # 1
    print bst.root.left.right.value  # 4
    print bst.root.right.left.value  # 7
    print bst.root.right.right.value  # 9

    print bst.root.left.left.left.value  # 0
    print bst.root.left.right.left.value  # 3
    print bst.root.right.left.left.value  # 6
