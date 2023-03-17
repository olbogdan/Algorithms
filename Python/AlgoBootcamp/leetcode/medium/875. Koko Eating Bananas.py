# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
# The guards have gone and will come back in h hours.
#
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile
# of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats
# all of them instead and will not eat any more bananas during this hour.
#
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
#
# Return the minimum integer k such that she can eat all the bananas within h hours.
# Example 1:
#
# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:
#
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# Example 3:
#
# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
#
#
# Constraints:
#
# 1 <= piles.length <= 104
# piles.length <= h <= 109
# 1 <= piles[i] <= 109
from math import inf
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # avrBananDay = sum(piles) // len(piles)
        # timeMultiplier = len(piles) / h
        # l = int(avrBananDay * timeMultiplier)
        l = 1
        r = max(piles)

        def canEat(bananas):
            hours = 0
            for b in piles:
                if b % bananas != 0:
                    hours += (b//bananas + 1)
                else:
                    hours += b//bananas
                if hours > h:
                    return False
            return hours <= h

        while l < r:
            mid = (l+r)//2
            if canEat(mid):
                r = mid
            else:
                l = mid + 1
        return l


sol = Solution()
assert sol.minEatingSpeed([312884470], 312884469) == 2
assert sol.minEatingSpeed([3,6,7,11], 8) == 4
assert sol.minEatingSpeed([312884470], 312884469) == 2
assert sol.minEatingSpeed([1000000000,1000000000], 3) == 1000000000


class Solution2:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = int(sum(piles) / len(piles) / h)
        if left == 0:
            left = 1
        right = max(piles)
        result = float(inf)

        def isValid(k):
            capacity = h
            for i in piles:
                daysToFinishOnePile = int(-(-i // k))
                capacity -= daysToFinishOnePile
                if capacity < 0:
                    return False
            return True

        while left <= right:
            mid = (left + right) // 2
            if isValid(mid):
                result = min(result, mid)
                right = mid - 1
            else:
                left = mid + 1
        return result


sol = Solution2()
assert sol.minEatingSpeed([3,6,7,11], 8) == 4
assert sol.minEatingSpeed([312884470], 312884469) == 2
assert sol.minEatingSpeed([1000000000,1000000000], 3) == 1000000000