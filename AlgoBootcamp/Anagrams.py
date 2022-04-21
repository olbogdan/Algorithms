import re


def anagrams(str1, str2):
    plainStr1 = re.sub("[\W]", "", str1).lower()
    plainStr2 = re.sub("[\W]", "", str2).lower()
    if len(plainStr1) != len(plainStr2):
        return False

    dict1 = {}
    for i in plainStr1:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] = dict1[i] + 1

    dict2 = {}
    for i in plainStr2:
        if i not in dict2:
            dict2[i] = 1
        else:
            dict2[i] = dict2[i] + 1

    for key, value in dict1.items():
        if key not in dict2 or dict2[key] != value:
            return False
    return True

print(anagrams("b aBx!", ",  babx"))