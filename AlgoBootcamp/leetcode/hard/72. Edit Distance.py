# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
#
# You have the following three operations permitted on a word:
#
# Insert a character
# Delete a character
# Replace a character
#
#
# Example 1:
#
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:
#
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
#
#
# Constraints:
#
# 0 <= word1.length, word2.length <= 500
# word1 and word2 consist of lowercase English letters.
from functools import cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dp(i, j):
            if i == len(word1) or j == len(word2):
                return max(len(word1)-i, len(word2)-j)
            if word1[i] == word2[j]:
                return dp(i+1, j+1)
            else:
                return 1 + min(dp(i+1, j+1), dp(i+1, j), dp(i, j+1))

        return dp(0, 0)


sol = Solution()
res = sol.minDistance("horse", "ros")
assert res == 3
res = sol.minDistance("intention", "execution")
assert res == 5


class Solution2:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def min_distance(i1: int, i2: int) -> int:
            if not i1 or not i2: return max(i1, i2)

            return (
                min_distance(i1 - 1, i2 - 1)
                if word1[i1 - 1] == word2[i2 - 1]
                else 1 + min(
                    min_distance(i1 - 1, i2 - 1),
                    min_distance(i1, i2 - 1),
                    min_distance(i1 - 1, i2),
                )
            )

        return min_distance(len(word1), len(word2))


sol = Solution2()
res = sol.minDistance("horse", "ros")
assert res == 3
res = sol.minDistance("intention", "execution")
assert res == 5


class Solution3:
    def minDistance(self, word1: str, word2: str) -> int:
        # w1 = "ab" w2 = "abc"
        # [
        #   [0, 0, 0]
        #   [0, 0, 0]
        # ]
        dp = [ [0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        # fill last rows with incremental 0-len() numbers
        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i

        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j+1], dp[i][j + 1], dp[i + 1][j]) + 1

        return dp[0][0]


sol = Solution3()
res = sol.minDistance("horse", "ros")
assert res == 3
res = sol.minDistance("intention", "execution")
assert res == 5
