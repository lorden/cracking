class Node:
    left = None
    right = None
    value = None

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "NODE: %s" % self.value


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


# Using python lists instead of linked lists

def create_level_linked_list(root):
    lists = []
    lists.append([root])  # First list
    current = [root]
    while len(current) > 0:
        parents = current
        current = []
        for parent in parents:
            if parent.left:
                current.append(parent.left)
            if parent.right:
                current.append(parent.right)

        if current:
            lists.append(current)
    return lists


if __name__ == '__main__':
    t = Tree()
    t.insert(3)
    t.insert(1)
    t.insert(5)
    t.insert(0)
    t.insert(2)
    t.insert(4)
    t.insert(6)
    lists = create_level_linked_list(t.root)
    for l in lists:
        values_list = []
        for node in l:
            values_list.append(node.value)
        print values_list
