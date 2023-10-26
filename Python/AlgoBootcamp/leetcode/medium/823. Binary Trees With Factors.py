# Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.
#
# We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.
#
# Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.
#
#
#
# Example 1:
#
# Input: arr = [2,4]
# Output: 3
# Explanation: We can make these trees: [2], [4], [4, 2, 2]
# Example 2:
#
# Input: arr = [2,4,5,10]
# Output: 7
# Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
#
#
# Constraints:
#
# 1 <= arr.length <= 1000
# 2 <= arr[i] <= 109
# All the values of arr are unique.
from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        dp = {}
        for i in range(len(arr)):
            root = arr[i]
            dp[root] = 1
            for candidate1 in arr:
                if candidate1 >= root:
                    break
                candidate2 = arr[i] // candidate1
                if root % candidate1 == 0 and candidate2 in dp:
                    dp[arr[i]] += dp[candidate1] * dp[candidate2]
        return sum(dp.values()) % MOD


sol = Solution()
assert sol.numFactoredBinaryTrees([2, 5, 10, 20]) == 12

#10

#10
#5 2

#10
#2 5

#20

#20
#10 2

#20
#2 10


