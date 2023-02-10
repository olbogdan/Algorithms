# You are given an array of strings ideas that represents a list of names to be used in the process of naming a company. The process of naming a company is as follows:
#
# Choose 2 distinct names from ideas, call them ideaA and ideaB.
# Swap the first letters of ideaA and ideaB with each other.
# If both of the new names are not found in the original ideas, then the name ideaA ideaB (the concatenation of ideaA and ideaB, separated by a space) is a valid company name.
# Otherwise, it is not a valid name.
# Return the number of distinct valid names for the company.
# Example 1:
#
# Input: ideas = ["coffee","donuts","time","toffee"]
# Output: 6
# Explanation: The following selections are valid:
# - ("coffee", "donuts"): The company name created is "doffee conuts".
# - ("donuts", "coffee"): The company name created is "conuts doffee".
# - ("donuts", "time"): The company name created is "tonuts dime".
# - ("donuts", "toffee"): The company name created is "tonuts doffee".
# - ("time", "donuts"): The company name created is "dime tonuts".
# - ("toffee", "donuts"): The company name created is "doffee tonuts".
# Therefore, there are a total of 6 distinct company names.
#
# The following are some examples of invalid selections:
# - ("coffee", "time"): The name "toffee" formed after swapping already exists in the original array.
# - ("time", "toffee"): Both names are still the same after swapping and exist in the original array.
# - ("coffee", "toffee"): Both names formed after swapping already exist in the original array.
# Example 2:
#
# Input: ideas = ["lack","back"]
# Output: 0
# Explanation: There are no valid selections. Therefore, 0 is returned.
#
#
# Constraints:
#
# 2 <= ideas.length <= 5 * 104
# 1 <= ideas[i].length <= 10
# ideas[i] consists of lowercase English letters.
# All the strings in ideas are unique.
from collections import defaultdict
from typing import List


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        words = defaultdict(set)
        for s in ideas:
            words[s[0]].add(s[1:])

        result = 0
        # visited = set() Possible optimisation
        for key1, set1 in words.items():
            for key2, set2 in words.items():
                if key1 == key2:
                    continue
                # if (key2, key1) in visited:
                #     continue
                # visited.add((key1, key2))
                intersects = 0
                for w in set1:
                    if w in set2:
                        intersects += 1
                unicWords1 = len(set1) - intersects
                unicWords2 = len(set2) - intersects
                result += unicWords1 * unicWords2  # * 2 Possible optimisation
        return result


sol = Solution()
res = sol.distinctNames(["coffee","donuts","time","toffee"])
assert res == 6
res = sol.distinctNames(["lack","back"])
assert res == 0
