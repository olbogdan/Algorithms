# You are given a large integer represented as an integer array digits,
# where each digits[i] is the ith digit of the integer. The digits are
# ordered from most significant to least significant in left-to-right order.
# The large integer does not contain any leading 0's.
#
# Increment the large integer by one and return the resulting array of digits.


class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        memo = 1
        for i in range(len(digits) - 1, -1, -1):
            num = digits[i]
            if num == 9 and memo:
                num = 0
            else:
                num += memo
                memo = 0
            digits[i] = num

        if memo:
            return [1] + digits
        return digits


sol = Solution()
assert sol.plusOne([1, 2, 3]) == [1, 2, 4]
assert sol.plusOne([9]) == [1, 0]
assert sol.plusOne([0]) == [1]
