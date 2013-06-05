def unique_chars(input):
    sorted_input = sorted(input)
    prev = ''
    for c in sorted_input:
        if prev != c:
            prev = c
        else:
            return False
    return True

input = raw_input("Enter string: ")
if unique_chars(input):
    print "All unique characters"
else:
    print "Not all unique characters"
