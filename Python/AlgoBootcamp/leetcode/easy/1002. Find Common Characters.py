# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
#
#
#
# Example 1:
#
# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:
#
# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]
#
#
# Constraints:
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of lowercase English letters.


from collections import Counter
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = Counter(words[0])
        for i in range(1, len(words)):
            nextLevel = {}
            candidate = Counter(words[i])
            for k, v in candidate.items():
                if k in res:
                    nextLevel[k] = min(candidate[k], res[k])
            res = nextLevel
        result = []
        for k, v in res.items():
            for _ in range(v):
                result.append(k)
        return result


sol = Solution()
assert sol.commonChars(["bella", "label", "roller"]) == ["l", "l", "e"]
assert sol.commonChars(["cool", "lock", "cook"]) == ["c", "o"]
