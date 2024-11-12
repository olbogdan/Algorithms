# You are given a 0-indexed integer array nums of length n.
#
# You can perform the following operation as many times as you want:
#
# Pick an index i that you haven’t picked before, and pick a prime p strictly less than nums[i], then subtract p from nums[i].
# Return true if you can make nums a strictly increasing array using the above operation and false otherwise.
#
# A strictly increasing array is an array whose each element is strictly greater than its preceding element.
#
#
#
# Example 1:
#
# Input: nums = [4,9,6,10]
# Output: true
# Explanation: In the first operation: Pick i = 0 and p = 3, and then subtract 3 from nums[0], so that nums becomes [1,9,6,10].
# In the second operation: i = 1, p = 7, subtract 7 from nums[1], so nums becomes equal to [1,2,6,10].
# After the second operation, nums is sorted in strictly increasing order, so the answer is true.
# Example 2:
#
# Input: nums = [6,8,11,12]
# Output: true
# Explanation: Initially nums is sorted in strictly increasing order, so we don't need to make any operations.
# Example 3:
#
# Input: nums = [5,8,3]
# Output: false
# Explanation: It can be proven that there is no way to perform operations to make nums sorted in strictly increasing order, so the answer is false.
#
#
# Constraints:
#
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 1000
# nums.length == n
from math import sqrt
from typing import List


class Solution:
    def getPrimes(self, nums: List[int]) -> List[int]:
        maxNum = max(nums)
        res = []  # num to factor list
        for i in range(2, maxNum + 1):
            isPrime = True
            for factor in range(2, int(sqrt(i)) + 1):
                if i % factor == 0:
                    isPrime = False
                    break
            if isPrime:
                res.append(i)
        return res

    def primeSubOperation(self, nums: List[int]) -> bool:
        primes = self.getPrimes(nums)
        prevNum = 0  # lower border, new value should be bigger then this
        for n in nums:
            nextNum = n
            for p in reversed(primes):
                if n - p > prevNum:
                    nextNum = n - p
                    break
            if prevNum >= nextNum:
                return False
            prevNum = nextNum
        return True


s = Solution()
assert s.primeSubOperation([4, 9, 6, 10]) is True
assert s.primeSubOperation([6, 8, 11, 12]) is True
assert s.primeSubOperation([5,8,3]) is False
