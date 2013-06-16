from base import Node, print_nodes


def sum_linked_lists(root1, root2):
    num1 = 0
    mult = 1
    while root1 is not None:
        num1 += root1.data * mult
        root1 = root1.next
        mult *= 10
    num2 = 0
    mult = 1
    while root2 is not None:
        num2 += root2.data * mult
        root2 = root2.next
        mult *= 10
    result = num1 + num2
    print "%s + %s = %s" % (num1, num2, result)
    result_list = None
    for x in str(result)[::-1]:
        if result_list is None:
            result_list = Node(x)
        else:
            result_list.append_to_tail(x)
    return result_list


root1 = Node(3)
root1.append_to_tail(1)
root1.append_to_tail(5)
root1.append_to_tail(6)

root2 = Node(5)
root2.append_to_tail(9)
root2.append_to_tail(2)

result = sum_linked_lists(root1, root2)
print_nodes(result)
