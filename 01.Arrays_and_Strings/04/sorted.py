def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

str1 = raw_input("String 1: ")
str2 = raw_input("String 2: ")
print are_anagrams(str1, str2)
