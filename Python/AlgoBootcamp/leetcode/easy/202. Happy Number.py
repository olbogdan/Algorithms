# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.
# Example 1:
#
# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# Example 2:
#
# Input: n = 2
# Output: false
# Constraints:
#
# 1 <= n <= 231 - 1


class Solution:
    def isHappy(self, n: int) -> bool:
        memo = set()
        while n != 1:
            subSum = 0

            # 10 % 10 == 0
            # 10 // 10 == 1
            # 1 % 10 == 1
            # 1 // 10 == 0
            subN = n
            while subN != 0:
                subSum += (subN % 10) ** 2
                subN = subN // 10

            if subSum in memo:
                return False
            memo.add(subSum)
            n = subSum
        return True


sol = Solution()
assert sol.isHappy(19) is True
assert sol.isHappy(2) is False


class Solution2:
    def isHappy(self, n: int) -> bool:
        memo = set()
        while n != 1:
            z = 0
            for x in str(n):
                z += int(x)**2
            n = z
            if z in memo:
                return False
            memo.add(z)
        return True


sol = Solution2()
assert sol.isHappy(19) is True
assert sol.isHappy(2) is False
