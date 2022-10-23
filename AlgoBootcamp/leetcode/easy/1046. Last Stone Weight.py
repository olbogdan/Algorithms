# You are given an array of integers stones where stones[i] is the weight of the ith stone.
#
# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
#
# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.
#
# Return the weight of the last remaining stone. If there are no stones left, return 0.
# Example 1:
#
# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
# Example 2:
#
# Input: stones = [1]
# Output: 1
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # since python does not have max heap, we will simulate a max heap by using a min heap,
        # for this we change a sign of each item of the array to negative,
        # so heaviest will be the lightest, and it will be at the top of the heap.
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapify(stones)
        while len(stones) > 1:
            # heappop returns the heaviest stone (we need to change its sign back to positive(+),
            # since it was inverted by us in the previous step)
            x = -heappop(stones)
            y = -heappop(stones)
            # smash two heaviest stones
            weight = x - y
            # is some weight left after smash, store it to the heap
            if weight > 0:
                heappush(stones, -weight)
        if stones:
            return -stones[0]
        else:
            return 0


solution = Solution()
assert solution.lastStoneWeight([2,7,4,1,8,1]) == 1
assert solution.lastStoneWeight([2,2]) == 0


