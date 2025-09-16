# You are given an array of integers nums. Perform the following steps:
#
# Find any two adjacent numbers in nums that are non-coprime.
# If no such numbers are found, stop the process.
# Otherwise, delete the two numbers and replace them with their LCM (Least Common Multiple).
# Repeat this process as long as you keep finding two adjacent non-coprime numbers.
# Return the final modified array. It can be shown that replacing adjacent non-coprime numbers in any arbitrary order will lead to the same result.
#
# The test cases are generated such that the values in the final array are less than or equal to 108.
#
# Two values x and y are non-coprime if GCD(x, y) > 1 where GCD(x, y) is the Greatest Common Divisor of x and y.
#
#
#
# Example 1:
#
# Input: nums = [6,4,3,2,7,6,2]
# Output: [12,7,6]
# Explanation:
# - (6, 4) are non-coprime with LCM(6, 4) = 12. Now, nums = [12,3,2,7,6,2].
# - (12, 3) are non-coprime with LCM(12, 3) = 12. Now, nums = [12,2,7,6,2].
# - (12, 2) are non-coprime with LCM(12, 2) = 12. Now, nums = [12,7,6,2].
# - (6, 2) are non-coprime with LCM(6, 2) = 6. Now, nums = [12,7,6].
# There are no more adjacent non-coprime numbers in nums.
# Thus, the final modified array is [12,7,6].
# Note that there are other ways to obtain the same resultant array.
# Example 2:
#
# Input: nums = [2,2,1,1,3,3,3]
# Output: [2,1,1,3]
# Explanation:
# - (3, 3) are non-coprime with LCM(3, 3) = 3. Now, nums = [2,2,1,1,3,3].
# - (3, 3) are non-coprime with LCM(3, 3) = 3. Now, nums = [2,2,1,1,3].
# - (2, 2) are non-coprime with LCM(2, 2) = 2. Now, nums = [2,1,1,3].
# There are no more adjacent non-coprime numbers in nums.
# Thus, the final modified array is [2,1,1,3].
# Note that there are other ways to obtain the same resultant array.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
# The test cases are generated such that the values in the final array are less than or equal to 108.


class Solution:
    def replaceNonCoprimes(self, nums):
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        stack = []
        for x in nums:
            stack.append(x)

            while len(stack) > 1:
                a, b = stack[-2], stack[-1]
                g = gcd(a, b)
                if g == 1:
                    break
                lcm = a * b // g
                stack.pop()
                stack[-1] = lcm
        return stack


sol = Solution()
assert sol.replaceNonCoprimes([6, 4, 3, 2, 7, 6, 2]) == [12, 7, 6]
assert sol.replaceNonCoprimes([2, 2, 1, 1, 3, 3, 3]) == [2, 1, 1, 3]
