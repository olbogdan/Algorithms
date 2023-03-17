# You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.
#
# Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

def areAlmostEqual(s1: str, s2: str) -> bool:
    if s1 == s2:
        return True
    firstDiff = -1
    secondDiff = -1

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if firstDiff == -1:
                firstDiff = i
            elif secondDiff == -1:
                secondDiff = i
            else:
                return False
    return s1[firstDiff] == s2[secondDiff] and s1[secondDiff] == s2[firstDiff]

assert areAlmostEqual("bank", "kanb") == True
assert areAlmostEqual("aaaa", "aaaa") == True
assert areAlmostEqual("qgqeg", "gqgeq") == False
assert areAlmostEqual("aa", 'ac') == False
assert areAlmostEqual("attack", "defend") == False


def areAlmostEqual2(s1: str, s2: str) -> bool:
    found = ""
    required = ""

    maxOneSwapReached = False
    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            if maxOneSwapReached:
                return False

            if found == "":
                found = s1[i]
                required = s2[i]
            else:
                if s1[i] == required and s2[i] == found:
                    maxOneSwapReached = True
                else:
                    return False

    if found != "" and maxOneSwapReached == False:
        return False
    return True


assert areAlmostEqual2("bank", "kanb") == True
assert areAlmostEqual2("aaaa", "aaaa") == True
assert areAlmostEqual2("qgqeg", "gqgeq") == False
assert areAlmostEqual2("aa", 'ac') == False
assert areAlmostEqual2("attack", "defend") == False


def areAlmostEqual3(s1: str, s2: str) -> bool:
    if s1 == s2:
        return True
    s1 = list(s1)
    s2 = list(s2)
    oneSwapDone = False

    diffIndex1 = -1
    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            if diffIndex1 != -1 and oneSwapDone:
                return False
            elif diffIndex1 != -1:
                s1[i], s1[diffIndex1] = s1[diffIndex1], s1[i]
                oneSwapDone = True
            else:
                diffIndex1 = i

    return s1 == s2


assert areAlmostEqual3("bank", "kanb") == True
assert areAlmostEqual3("aaaa", "aaaa") == True
assert areAlmostEqual3("qgqeg", "gqgeq") == False
assert areAlmostEqual3("aa", 'ac') == False
assert areAlmostEqual3("attack", "defend") == False
