def remove_duplicates(string):
    clean = ''
    for c in string:
        if c not in clean:
            clean += c
    return clean

string = raw_input("Enter string: ")
print remove_duplicates(string)

### Test cases ###
# "abcdef"
# "aaabcdef"
# "abcdefff"
# "aaaaaaaa"
# "aaabcaaa"
# "abcdabcd"
# ""
