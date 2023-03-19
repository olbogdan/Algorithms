# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
#
# You can use each character in text at most once. Return the maximum number of instances that can be formed.
#
#
#
# Example 1:
#
#
#
# Input: text = "nlaebolko"
# Output: 1
# Example 2:
#
#
#
# Input: text = "loonbalxballpoon"
# Output: 2
# Example 3:
#
# Input: text = "leetcode"
# Output: 0
#
#
# Constraints:
#
# 1 <= text.length <= 104
# text consists of lower case English letters only.
from cmath import inf
from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        charRep = Counter(text)
        minRep = float(inf)
        repeatedChar = {"l", "o"}
        for c in "balon":
            reps = charRep[c]
            if c in repeatedChar:
                reps = reps // 2
            minRep = min(minRep, reps)
        return minRep


sol = Solution()
assert sol.maxNumberOfBalloons("loonbalxballpoon") == 2
