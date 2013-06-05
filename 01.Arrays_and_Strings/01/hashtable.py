def unique_chars(input):
    ht = {}
    for c in input:
        if c in ht:
            return False
        else:
            ht[c] = True
    return True

input = raw_input("Enter string: ")
if unique_chars(input):
    print "All unique characters"
else:
    print "Not all unique characters"
