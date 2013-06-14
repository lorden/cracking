def are_anagrams(str1, str2):
    dict1 = {}
    dict2 = {}
    for c in str1:
        if c in dict1:
            dict1[c] += 1
        else:
            dict1[c] = 1
    for c in str2:
        if c in dict2:
            dict2[c] += 1
        else:
            dict2[c] = 1
    return dict1 == dict2

str1 = raw_input("String 1: ")
str2 = raw_input("String 2: ")
print are_anagrams(str1, str2)
