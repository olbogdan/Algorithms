# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
#
# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.
#
#
#
# Example 1:
#
# Input: low = 100, high = 300
# Output: [123,234]
# Example 2:
#
# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]
#
#
# Constraints:
#
# 10 <= low <= high <= 10^9
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        model = "123456789"
        result = []
        N = len(model)
        i = 0
        for i in range(N):
            for j in range(i + 1, N + 1):
                num = int(model[i:j])
                if low <= num <= high:
                    result.append(num)
        result.sort()
        return result


sol = Solution()
assert sol.sequentialDigits(1000, 13000) == [1234,2345,3456,4567,5678,6789,12345]
