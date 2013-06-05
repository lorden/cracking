test = raw_input("Enter string: ")
test += "\0"
print 'Test string: %s' % test
print 'HEX => ' + ':'.join(x.encode('hex') for x in test)


def reverse_string(string):
    r = string[::-1]  # Reverse whole string
    r = r[1:]  # Remove first NULL
    r += "\0"  # Add NULL
    return r

test_reversed = reverse_string(test)
print 'Test string: %s' % test_reversed
print 'HEX => ' + ':'.join(x.encode('hex') for x in test_reversed)
