# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.
#
#
#
# Example 1:
#
# Input: arr = [5,5,4], k = 1
# Output: 1
# Explanation: Remove the single 4, only 5 is left.
# Example 2:
# Input: arr = [4,3,1,1,3,3,2], k = 3
# Output: 2
# Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
#
#
# Constraints:
#
# 1 <= arr.length <= 10^5
# 1 <= arr[i] <= 10^9
# 0 <= k <= arr.length

from collections import Counter
from heapq import heapify, heappush, heappop


class Solution:
    def findLeastNumOfUniqueInts(self, arr, k: int) -> int:
        counter = Counter(arr)
        prq = [] # [(count, number)]
        for key, val in counter.items():
            prq.append((val, key))
        heapify(prq)
        while k > 0:
            count, n = heappop(prq)
            if k >= count:
                k -= count
                continue
            heappush(prq, (count - k, n))
            break

        return len(prq)


sol = Solution()
assert sol.findLeastNumOfUniqueInts([5,5,4], 1) == 1
assert sol.findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 3) == 2
