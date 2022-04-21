import re

def anagrams3(str1, str2):
    plainStr1 = ""
    for i in str1.lower():
        if ord(i) in range(ord('a'), ord('z') + 1):
            plainStr1 += i
    plainStr2 = ""
    for i in str2.lower():
        if "a" <= i <= "z":
            plainStr2 += i

    dict1 = {}
    for i in plainStr1:
        dict1[i] = dict1.get(i, 0) + 1

    dict2 = {}
    for i in plainStr2:
        dict2[i] = dict2.get(i, 0) + 1

    return dict1 == dict2

print(anagrams3("b aBx!", ",  babx"))

def anagrams2(str1, str2):
    plainStr1 = "".join(filter(lambda s: s.isalpha(), str1)).lower()
    plainStr2 = "".join(filter(lambda s: s.isalpha(), str2)).lower()

    dict1 = {}
    for i in plainStr1:
        dict1[i] = dict1.get(i, 0) + 1

    dict2 = {}
    for i in plainStr2:
        dict2[i] = dict2.get(i, 0) + 1

    return dict1 == dict2

print(anagrams2("b aBx!", ",  babx"))

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

    return dict1 == dict2

print(anagrams("b aBx!", ",  babx"))