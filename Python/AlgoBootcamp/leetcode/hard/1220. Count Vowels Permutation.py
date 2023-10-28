# Given an integer n, your task is to count how many strings of length n can be formed under the following rules:
#
# Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
# Each vowel 'a' may only be followed by an 'e'.
# Each vowel 'e' may only be followed by an 'a' or an 'i'.
# Each vowel 'i' may not be followed by another 'i'.
# Each vowel 'o' may only be followed by an 'i' or a 'u'.
# Each vowel 'u' may only be followed by an 'a'.
# Since the answer may be too large, return it modulo 10^9 + 7.
#
#
#
# Example 1:
#
# Input: n = 1
# Output: 5
# Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
# Example 2:
#
# Input: n = 2
# Output: 10
# Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
# Example 3:
#
# Input: n = 5
# Output: 68
#
#
# Constraints:
#
# 1 <= n <= 2 * 10^4
from functools import cache


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dictionary = {}
        dictionary['a'] = ['e']
        dictionary['e'] = ['a', 'i']
        dictionary['i'] = ['a', 'e', 'o', 'u']
        dictionary['o'] = ['i', 'u']
        dictionary['u'] = ['a']

        @cache
        def dfs(vowel, level):
            if level == n:
                return 1
            result = 0
            for followed in dictionary[vowel]:
                result += dfs(followed, level + 1)
            return result

        result = 0
        MOD = 10 ** 9 + 7
        for vowel in ['a', 'e', 'i', 'o', 'u']:
            result += dfs(vowel, 1) % MOD
        return result % MOD


sol = Solution()
assert sol.countVowelPermutation(2) == 10
