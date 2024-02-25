# You are given a 0-indexed integer array nums, and you are allowed to traverse between its indices. You can traverse between index i and index j, i != j, if and only if gcd(nums[i], nums[j]) > 1, where gcd is the greatest common divisor.
#
# Your task is to determine if for every pair of indices i and j in nums, where i < j, there exists a sequence of traversals that can take us from i to j.
#
# Return true if it is possible to traverse between all such pairs of indices, or false otherwise.
#
#
#
# Example 1:
#
# Input: nums = [2,3,6]
# Output: true
# Explanation: In this example, there are 3 possible pairs of indices: (0, 1), (0, 2), and (1, 2).
# To go from index 0 to index 1, we can use the sequence of traversals 0 -> 2 -> 1, where we move from index 0 to index 2 because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1, and then move from index 2 to index 1 because gcd(nums[2], nums[1]) = gcd(6, 3) = 3 > 1.
# To go from index 0 to index 2, we can just go directly because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1. Likewise, to go from index 1 to index 2, we can just go directly because gcd(nums[1], nums[2]) = gcd(3, 6) = 3 > 1.
# Example 2:
#
# Input: nums = [3,9,5]
# Output: false
# Explanation: No sequence of traversals can take us from index 0 to index 2 in this example. So, we return false.
# Example 3:
#
# Input: nums = [4,3,12,8]
# Output: true
# Explanation: There are 6 possible pairs of indices to traverse between: (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), and (2, 3). A valid sequence of traversals exists for each pair, so we return true.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
from typing import List


class UnionFind:
    def __init__(self, n):
        self.count = n
        self.par = [i for i in range(n)]
        self.depth = [1] * n

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return
        if self.depth[rootX] > self.depth[rootY]:
            self.par[rootX] = rootY
            self.depth[rootX] += self.depth[rootY]
        else:
            self.par[rootY] = rootX
            self.depth[rootY] += self.depth[rootX]
        self.count -= 1


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = UnionFind(len(nums))
        factorAdj = {}  # factor : indexes
        for idx, num in enumerate(nums):
            f = 2
            while f * f <= num:
                if num % f == 0:
                    # already found some number with same factor
                    if f in factorAdj:
                        uf.union(idx, factorAdj[f])
                    else:
                        factorAdj[f] = idx
                    # eleminate duplicates, factor 2, target 6
                    while num % f == 0:
                        num = num // f
                f += 1
            if num > 1:
                if num in factorAdj:
                    uf.union(idx, factorAdj[num])
                else:
                    factorAdj[num] = idx
        return uf.count == 1


sol = Solution()
assert sol.canTraverseAllPairs([2, 3, 6]) is True
assert sol.canTraverseAllPairs([3, 9, 5]) is False
