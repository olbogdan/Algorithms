# Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.
#
# You must write an algorithm that runs in O(n) time and uses O(1) extra space.
#
#
#
# Example 1:
#
# Input: n = 13
# Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
# Example 2:
#
# Input: n = 2
# Output: [1,2]
#
#
# Constraints:
#
# 1 <= n <= 5 * 104
from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        i = 1
        while len(res) < n:
            res.append(i)
            if i * 10 <= n:
                i = i * 10
            else:
                while i >= n or i % 10 == 9:
                    i = i // 10
                i += 1
        return res


sol = Solution()
assert sol.lexicalOrder(13) == [1,10,11,12,13,2,3,4,5,6,7,8,9]
assert sol.lexicalOrder(2) == [1,2]