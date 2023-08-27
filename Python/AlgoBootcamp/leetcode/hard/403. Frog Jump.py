# A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.
#
# Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.
#
# If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.
#
#
#
# Example 1:
#
# Input: stones = [0,1,3,5,6,8,12,17]
# Output: true
# Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.
# Example 2:
#
# Input: stones = [0,1,2,3,4,8,9,11]
# Output: false
# Explanation: There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.
#
#
# Constraints:
#
# 2 <= stones.length <= 2000
# 0 <= stones[i] <= 231 - 1
# stones[0] == 0
# stones is sorted in a strictly increasing order.
from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        N = len(stones)
        memo = {}

        def dp(curPosition, prevJump):
            if curPosition == N - 1:
                return True
            elif curPosition >= N or curPosition < 0:
                return False
            if (curPosition, prevJump) in memo:
                return memo[(curPosition, prevJump)]

            candidateTarget = stones[curPosition] + prevJump  # +/- 1
            t1 = self.findAvailableJump(stones, curPosition + 1, candidateTarget)
            if dp(t1, prevJump):
                return True

            t2 = self.findAvailableJump(stones, curPosition + 1, candidateTarget - 1)
            if dp(t2, prevJump - 1):
                return True

            t3 = self.findAvailableJump(stones, curPosition + 1, candidateTarget + 1)
            if dp(t3, prevJump + 1):
                return True

            memo[(curPosition, prevJump)] = False
            return False

        if stones[1] - stones[0] > 1:
            return False
        return dp(1, 1)

    def findAvailableJump(self, stones: List[int], fromIdx: int, target: int):
        l = fromIdx
        r = len(stones) - 1
        while l <= r:
            mid = (l + r) // 2
            if stones[mid] < target:
                l = mid + 1
            elif stones[mid] > target:
                r = mid - 1
            else:
                return mid
        return -1


sol = Solution()
res = sol.canCross([0,1,3,5])
assert res is True
res = sol.canCross([0,1,3,5,10])
assert res is False
