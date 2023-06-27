# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
#
# Define a pair (u, v) which consists of one element from the first array and one element from the second array.
#
# Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.
#
#
#
# Example 1:
#
# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Output: [[1,2],[1,4],[1,6]]
# Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
# Example 2:
#
# Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# Output: [[1,1],[1,1]]
# Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
# Example 3:
#
# Input: nums1 = [1,2], nums2 = [3], k = 3
# Output: [[1,3],[2,3]]
# Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
#
#
# Constraints:
#
# 1 <= nums1.length, nums2.length <= 105
# -109 <= nums1[i], nums2[i] <= 109
# nums1 and nums2 both are sorted in ascending order.
# 1 <= k <= 104
from heapq import heappop, heappush
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        N1, N2 = len(nums1), len(nums2)
        visited = set()
        hp = []
        hp.append((nums1[0] + nums2[0], (0, 0)))
        visited.add((0, 0))
        count = 0
        while k and hp:
            _, [i, j] = heappop(hp)
            ans.append([nums1[i], nums2[j]])

            if i+1 < N1 and (i+1,j) not in visited:
                heappush(hp, (nums1[i + 1] + nums2[j], [i + 1, j]))
                visited.add((i + 1, j))

            if j+1 < N2 and (i, j+1) not in visited:
                heappush(hp, (nums1[i] + nums2[j + 1], [i, j + 1]))
                visited.add((i, j + 1))

            k -= 1

        return ans


sol = Solution()
sol.kSmallestPairs([1,1,2], [1,2,3], 2) == [[1,1],[1,1]]


class Solution2:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq = [] # [sum : (val1, val2)]

        for n1 in nums1:
            for n2 in nums2:
                newSum = (n1 + n2) * -1 # make max heap by inversing the value
                if len(pq) < k:
                    heappush(pq, (newSum, [n1, n2]))
                elif pq[0][0] < newSum:
                    heappop(pq)
                    heappush(pq, (newSum, [n1, n2]))
        result = []
        while pq:
            result.append(heappop(pq)[1])
        result.reverse()
        return result


sol = Solution2()
sol.kSmallestPairs([1,1,2], [1,2,3], 2) == [[1,1],[1,1]]
