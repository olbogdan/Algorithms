# Given an integer n, return any array containing n unique integers such that they add up to 0.
#
#
#
# Example 1:
#
# Input: n = 5
# Output: [-7,-1,1,3,4]
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
# Example 2:
#
# Input: n = 3
# Output: [-1,0,1]
# Example 3:
#
# Input: n = 1
# Output: [0]
#
#
# Constraints:
#
# 1 <= n <= 1000
from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        i = 0
        res = []
        while n > 0:
            if n % 2 != 0:
                res.append(0)
            else:
                i += 1
                res.extend([-i, i])
                n -= 1
            n -= 1
        return res


sol = Solution()
assert sol.sumZero(5) == [0, -1, 1, -2, 2,]
assert sol.sumZero(3) == [0, -1, 1]
assert sol.sumZero(1) == [0]
