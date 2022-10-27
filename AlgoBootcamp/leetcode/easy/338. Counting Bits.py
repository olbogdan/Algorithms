# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of
# 1's in the binary representation of i.
# Example 1:
#
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:
#
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
#
#
# Constraints:
#
# 0 <= n <= 105
#
#
# Follow up:
#
# It is very easy to come up with a solution with a runtime of O(n log n). Can you
# do it in linear time O(n) and possibly in a single pass?
# Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
from typing import List


# 0 - 0000
# 1 - 0001
# 2 - 0010
# 3 - 0011
# 4 - 0100
# 5 - 0101
# 6 - 0110
# 7 - 0111
# 8 - 1000
# 9 - 1001
# 10 - 1010
# you can see if we shift 5 to the right by 1, and it becomes 2, and 5 & 1 is 1, so the number of 1's in 5, is actually
# the number of 1's in 2 plus 1, because 5&1 == 1.
# similarly if we shift 4 to the right by 1, which becomes 2 as well, and 4&1 is 0, so number of 1's in 4, is the the number
# of 1's in 2 plus 0, because 4&1 == 0.
class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        for i in range(len(result)):
            # result of i=8 and 9 result[8 >> 1] and result[9 >> 1] is the same [4 == 0100],
            # but 9 has additional a at the beginning 1 that we can get by i & 1
            result[i] = result[i >> 1] + (i & 1)
        return result


solution = Solution()
assert solution.countBits(2) == [0,1,1]
assert solution.countBits(10) == [0,1,1,2,1,2,2,3,1,2,2]