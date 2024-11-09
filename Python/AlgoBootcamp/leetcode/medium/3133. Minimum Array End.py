# You are given two integers n and x. You have to construct an array of positive integers nums of size n where for every 0 <= i < n - 1, nums[i + 1] is greater than nums[i], and the result of the bitwise AND operation between all elements of nums is x.
#
# Return the minimum possible value of nums[n - 1].
#
#
#
# Example 1:
#
# Input: n = 3, x = 4
#
# Output: 6
#
# Explanation:
#
# nums can be [4,5,6] and its last element is 6.
#
# Example 2:
#
# Input: n = 2, x = 7
#
# Output: 15
#
# Explanation:
#
# nums can be [7,15] and its last element is 15.
#
#
#
# Constraints:
#
# 1 <= n, x <= 108


class Solution1:
    def minEnd(self, n: int, x: int) -> int:
        curNum = x
        while n > 1:
            curNum += 1
            curNum = curNum | x
            n -= 1
        return curNum


sol = Solution1()
assert sol.minEnd(3, 4) == 6
assert sol.minEnd(2, 7) == 15


class Solution2:
    def minEnd(self, n: int, x: int) -> int:
        pos = 0
        n -= 1
        while n > 0:
            bit = n & 1
            n = n >> 1
            while x & (1 << pos) > 0:
                pos += 1
            x = x ^ bit << pos
            pos += 1
        return x


sol = Solution2()
assert sol.minEnd(3, 4) == 6
assert sol.minEnd(2, 7) == 15
