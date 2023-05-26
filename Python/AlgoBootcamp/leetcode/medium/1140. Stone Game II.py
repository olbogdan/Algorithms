# Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones.
#
# Alice and Bob take turns, with Alice starting first.  Initially, M = 1.
#
# On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).
#
# The game continues until all the stones have been taken.
#
# Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.
#
#
#
# Example 1:
#
# Input: piles = [2,7,9,4,4]
# Output: 10
# Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger.
# Example 2:
#
# Input: piles = [1,2,3,4,5,100]
# Output: 104
#
#
# Constraints:
#
# 1 <= piles.length <= 100
# 1 <= piles[i] <= 104
from cmath import inf
from functools import cache
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # M -> amount of stones can be taken, starts from 1
        # i -> idx of stone in a piles, start from 0
        # alowence stones to take in a range from [1 to 2 * M]
        # example for M = 1 -> [1, 2]
        # example for M = 2 -> [1, 2, 3, 4]
        @cache
        def dp(alise, idx, M):
            if idx == len(piles):
                return 0

            maxPileSize = M * 2

            prefixSum = 0
            maximiseAlise = 0
            if alise:
                for X in range(1, maxPileSize + 1):  # [1, max(inclusive)]
                    if idx + X > len(piles):
                        break
                    prefixSum += piles[idx + X - 1]
                    maximiseAlise = max(maximiseAlise, prefixSum + dp(not alise, idx + X, max(M, X)))
                return maximiseAlise

            minimiseAlise = float(inf)
            if not alise:
                for X in range(1, maxPileSize + 1):  # [1, max(inclusive)]
                    if idx + X > len(piles):
                        break
                    minimiseAlise = min(minimiseAlise, dp(not alise, idx + X, max(M, X)))

                return minimiseAlise

        return dp(True, 0, 1)


sol = Solution()
assert sol.stoneGameII([1,2,3,4,5,100]) == 104
assert sol.stoneGameII([2,7,9,4,4]) == 10
