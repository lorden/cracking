def is_substring(haystack, needle):
    return needle in haystack


def is_rotation(str1, str2):
    if len(str1) != len(str2):
        return False
    str1 += str1
    return is_substring(str1, str2)

str1 = raw_input('String 1: ')
str2 = raw_input('String 2: ')
print is_rotation(str1, str2)
