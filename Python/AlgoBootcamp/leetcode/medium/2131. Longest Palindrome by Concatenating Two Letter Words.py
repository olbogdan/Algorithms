# You are given an array of strings words. Each element of words consists of two lowercase English letters.
#
# Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.
#
# Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.
#
# A palindrome is a string that reads the same forward and backward.
#
#
#
# Example 1:
#
# Input: words = ["lc","cl","gg"]
# Output: 6
# Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
# Note that "clgglc" is another longest palindrome that can be created.
# Example 2:
#
# Input: words = ["ab","ty","yt","lc","cl","ab"]
# Output: 8
# Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
# Note that "lcyttycl" is another longest palindrome that can be created.
# Example 3:
#
# Input: words = ["cc","ll","xx"]
# Output: 2
# Explanation: One longest palindrome is "cc", of length 2.
# Note that "ll" is another longest palindrome that can be created, and so is "xx".
#
#
# Constraints:
#
# 1 <= words.length <= 105
# words[i].length == 2
# words[i] consists of lowercase English letters.
from typing import List, Counter


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # aa
        # bb bb
        # bbaabb -> start from odd add all pairs

        # aa
        # bb bb bb
        # bbaabb or bbbbbb -> all odd, take odd and + each odd-1

        # aa aa
        # bb bb bb bb
        # all combo valid for pairs

        # diff, such as ab
        # count all mirror, add even rounded count of mirrors
        res = 0
        counts = Counter(words)
        isOddTwinAdded = False
        for word, count in counts.items():
            isOdd = count % 2 == 1
            if word[0] == word[1]:
                if isOdd and not isOddTwinAdded:
                    isOddTwinAdded = True
                    res += (count * 2)
                else:
                    res += (count // 2 * 2) * 2
            else:
                count = min(count, counts[word[1]+word[0]])
                res += count * 2
        return res


sol = Solution()
print(sol.longestPalindrome(["lc", "cl", "gg"]))
# assert sol.longestPalindrome(["lc", "cl", "gg"]) == 6
# assert sol.longestPalindrome(["ab", "ty", "yt", "lc", "cl", "ab"]) == 8
