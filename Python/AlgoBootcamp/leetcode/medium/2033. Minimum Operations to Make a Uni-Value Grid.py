# You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.
#
# A uni-value grid is a grid where all the elements of it are equal.
#
# Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.
#
#
#
# Example 1:
#
#
# Input: grid = [[2,4],[6,8]], x = 2
# Output: 4
# Explanation: We can make every element equal to 4 by doing the following:
# - Add x to 2 once.
# - Subtract x from 6 once.
# - Subtract x from 8 twice.
# A total of 4 operations were used.
# Example 2:
#
#
# Input: grid = [[1,5],[2,3]], x = 1
# Output: 5
# Explanation: We can make every element equal to 3.
# Example 3:
#
#
# Input: grid = [[1,2],[3,4]], x = 2
# Output: -1
# Explanation: It is impossible to make every element equal.
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 105
# 1 <= m * n <= 105
# 1 <= x, grid[i][j] <= 104
from typing import List


class Solution:
    def minOperationsArr(self, arr: List[int], x: int) -> int:
        N = len(arr)
        mid = arr[N//2]
        res = 0
        for num in arr:
            diff = abs(num - mid)
            if diff % x != 0:
                return -1
            else:
                res += diff // x
        return res

    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                arr.append(grid[r][c])
        arr.sort()
        return self.minOperationsArr(arr, x)


sol = Solution()
assert sol.minOperations([[2,4],[6,8]], 2) == 4
assert sol.minOperations([[1,5],[2,3]], 1) == 5
assert sol.minOperations([[1,2],[3,4]], 2) == -1
