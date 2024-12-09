# An array is considered special if every pair of its adjacent elements contains two numbers with different parity.
#
# You are given an array of integer nums and a 2D integer matrix queries, where for queries[i] = [fromi, toi] your task is to check that
# subarray
#  nums[fromi..toi] is special or not.
#
# Return an array of booleans answer such that answer[i] is true if nums[fromi..toi] is special.
#
#
#
# Example 1:
#
# Input: nums = [3,4,1,2,6], queries = [[0,4]]
#
# Output: [false]
#
# Explanation:
#
# The subarray is [3,4,1,2,6]. 2 and 6 are both even.
#
# Example 2:
#
# Input: nums = [4,3,1,6], queries = [[0,2],[2,3]]
#
# Output: [false,true]
#
# Explanation:
#
# The subarray is [4,3,1]. 3 and 1 are both odd. So the answer to this query is false.
# The subarray is [1,6]. There is only one pair: (1,6) and it contains numbers with different parity. So the answer to this query is true.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
# 1 <= queries.length <= 105
# queries[i].length == 2
# 0 <= queries[i][0] <= queries[i][1] <= nums.length - 1
from typing import List


class Solution:
    def getLongestPostfix(self, nums: List[int]) -> List[bool]:
        res = []
        res.append(0)
        prevNumer = nums[-1]
        for i in reversed(range(0, len(nums) - 1)):
            num = nums[i]
            n1Even = (prevNumer % 2 == 0)
            n2Even = (num % 2 == 0)
            if (n1Even and n2Even) or (not n1Even and not n2Even):
                res.append(0)
            else:
                res.append(1 + res[-1])
            prevNumer = num
        return list(reversed(res))

    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        postfix = self.getLongestPostfix(nums)
        res = []
        for start, end in queries:
            window = end - start
            if postfix[start] >= window:
                res.append(True)
            else:
                res.append(False)
        return res


sol = Solution()
assert sol.isArraySpecial([4, 3, 1, 6], [[0, 2], [2, 3]]) == [False, True]
assert sol.isArraySpecial([3, 4, 1, 2, 6], [[0, 4]]) == [False]
