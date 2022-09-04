# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
#
# In other words, return true if one of s1's permutations is the substring of s2.
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    hashMapS1 = {}
    hashMapS2 = {}
    for i in range(len(s1)):
        hashMapS1[s1[i]] = hashMapS1.get(s1[i], 0) + 1
        hashMapS2[s2[i]] = hashMapS2.get(s2[i], 0) + 1

    if hashMapS1 == hashMapS2:
        return True

    left = 0
    for i in range(len(s1), len(s2)):
        if hashMapS2[s2[left]] > 1:
            hashMapS2[s2[left]] -= 1
        else:
            del hashMapS2[s2[left]]

        hashMapS2[s2[i]] = hashMapS2.get(s2[i], 0) + 1

        if hashMapS1 == hashMapS2:
            return True
        left += 1
    return False


assert checkInclusion("aa", "baab") == True
assert checkInclusion("baa", "baab") == True
assert checkInclusion("ab", "eidbaooo") == True
assert checkInclusion("eidbaooo", "eidbaooo") == True
assert checkInclusion("eidbaoooaofb", "eidbaooo") == False
assert checkInclusion("xx", "axdjobxjosxjxjxjx") == False