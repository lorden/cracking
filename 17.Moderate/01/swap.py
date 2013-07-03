def swap_in_place(n1, n2):
    n1 = n1 + n2
    n2 = n1 - n2
    n1 = n1 - n2
    return (n1, n2)


n1 = 15
n2 = -33

print "n1: %s - n2: %s" % swap_in_place(n1, n2)
