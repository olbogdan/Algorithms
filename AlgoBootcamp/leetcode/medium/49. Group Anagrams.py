# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

def groupAnagrams(strs: [str]) -> [[str]]:
    dict = {}
    for s in strs:
        sortedS = tuple(sorted(s))
        if sortedS in dict:
            dict[sortedS].append(s)
        else:
            dict[sortedS] = [s]
    result = []
    for value in dict.values():
        result.append(value)
    return result

assert groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
