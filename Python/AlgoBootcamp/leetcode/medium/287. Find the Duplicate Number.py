# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
#
# There is only one repeated number in nums, return this repeated number.
#
# You must solve the problem without modifying the array nums and uses only constant extra space.
# Example 1:
#
# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:
#
# Input: nums = [3,1,3,4,2]
# Output: 3
#
#
# Constraints:
#
# 1 <= n <= 105
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.
#
#
# Follow up:
#
# How can we prove that at least one duplicate number must exist in nums?
# Can you solve the problem in linear runtime complexity?
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # [3, 2, 1, 3(slow/fast)]
        # [1, 2(slow), 3(fast), 4, 4]
        slow = nums[nums[0]]
        fast = nums[slow]
        while slow != fast:
            # jump slow 1 step
            slow = nums[slow]
            # jump fast 2 steps
            fast = nums[nums[fast]]
        # slow/fast point to sthe head of a cycle
        # distance haed of cycle to tail of cycle == head node to tail of cycle
        # iterate from head node and head of cycle +1 till they meet at a tail
        p1 = nums[0]
        p2 = slow
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]
        return p1


solution = Solution()
assert solution.findDuplicate([1,3,4,2,2]) == 2
assert solution.findDuplicate([1,1,1,1,1]) == 1
assert solution.findDuplicate([1,1,1,2,1]) == 1
assert solution.findDuplicate([2,2,2]) == 2
assert solution.findDuplicate([1,2,3,1]) == 1


class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow


solution = Solution2()
assert solution.findDuplicate([1,3,4,2,2]) == 2
assert solution.findDuplicate([1,1,1,1,1]) == 1
assert solution.findDuplicate([1,1,1,2,1]) == 1
assert solution.findDuplicate([2,2,2]) == 2
assert solution.findDuplicate([1,2,3,1]) == 1

def findDuplicate(nums):
    length = len(nums)
    low = 0
    high = length - 1

    while low < high:
        mid = (low + high) // 2
        count = 0

        for i in range(length):
            if nums[i] <= mid:
                count += 1

        if count <= mid:
            low = mid + 1
        else:
            high = mid

    return low


assert findDuplicate([1,3,4,2,2]) == 2
assert findDuplicate([1,1,1,1,1]) == 1
assert findDuplicate([1,1,1,2,1]) == 1
assert findDuplicate([2,2,2]) == 2
assert findDuplicate([1,2,3,1]) == 1