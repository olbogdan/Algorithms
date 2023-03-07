# Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.
#
# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.
#
#
#
# Example 1:
#
# Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
# Example 2:
#
# Input: hand = [1,2,3,4,5], groupSize = 4
# Output: false
# Explanation: Alice's hand can not be rearranged into groups of 4.
#
#
#
# Constraints:
#
# 1 <= hand.length <= 104
# 0 <= hand[i] <= 109
# 1 <= groupSize <= hand.length
from collections import Counter
from heapq import heapify, heappop
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = Counter(hand)
        heap = list(count.keys())
        heapify(heap)
        while heap:
            start = heap[0]
            for i in range(start, start + groupSize):
                if i not in count:
                    return False
                count[i] -= 1

                if count[i] == 0:
                    # [5(count 2), i! 6(count 0), 7(count 2)]
                    if heap[0] != i:
                        return False
                    heappop(heap)
        return True


sol = Solution()
assert sol.isNStraightHand([8,10,12], 3) is False
assert sol.isNStraightHand([1,2,3,4,5], 4) is False
assert sol.isNStraightHand([1,2,3,6,2,3,4,7,8], 3) is True
