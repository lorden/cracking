def replace_blanks(string):
    return string.replace(' ', '%20')

string = raw_input("String: ")
print replace_blanks(string)
