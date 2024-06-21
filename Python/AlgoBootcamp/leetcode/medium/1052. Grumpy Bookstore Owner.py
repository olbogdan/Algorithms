# There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.
#
# On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.
#
# When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.
#
# The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.
#
# Return the maximum number of customers that can be satisfied throughout the day.
#
#
#
# Example 1:
#
# Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
# Output: 16
# Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes.
# The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
# Example 2:
#
# Input: customers = [1], grumpy = [0], minutes = 1
# Output: 1
#
#
# Constraints:
#
# n == customers.length == grumpy.length
# 1 <= minutes <= n <= 2 * 104
# 0 <= customers[i] <= 1000
# grumpy[i] is either 0 or 1.
from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        GRUMPY = 1
        window = 0

        def addToWindow(i):
            nonlocal window
            if grumpy[i] == GRUMPY:
                window += customers[i]

        def removeFromWindow(i):
            nonlocal window
            if grumpy[i] == GRUMPY:
                window -= customers[i]

        happyCustomers = 0
        biggestWindow = 0
        l = 0
        for r in range(len(customers)):
            addToWindow(r)
            while r + 1 - l > minutes:
                removeFromWindow(l)
                l += 1
            biggestWindow = max(biggestWindow, window)

            if grumpy[r] != GRUMPY:
                happyCustomers += customers[r]

        return biggestWindow + happyCustomers


s = Solution()
assert s.maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3) == 16
assert s.maxSatisfied([1], [0], 1) == 1
