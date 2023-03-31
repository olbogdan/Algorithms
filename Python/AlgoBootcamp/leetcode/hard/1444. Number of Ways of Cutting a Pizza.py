# Given a rectangular pizza represented as a rows x cols matrix containing the following characters: 'A' (an apple) and '.' (empty cell) and given the integer k. You have to cut the pizza into k pieces using k-1 cuts.
#
# For each cut you choose the direction: vertical or horizontal, then you choose a cut position at the cell boundary and cut the pizza into two pieces. If you cut the pizza vertically, give the left part of the pizza to a person. If you cut the pizza horizontally, give the upper part of the pizza to a person. Give the last piece of pizza to the last person.
#
# Return the number of ways of cutting the pizza such that each piece contains at least one apple. Since the answer can be a huge number, return this modulo 10^9 + 7.
#
#
#
# Example 1:
#
#
#
# Input: pizza = ["A..","AAA","..."], k = 3
# Output: 3
# Explanation: The figure above shows the three ways to cut the pizza. Note that pieces must contain at least one apple.
# Example 2:
#
# Input: pizza = ["A..","AA.","..."], k = 3
# Output: 1
# Example 3:
#
# Input: pizza = ["A..","A..","..."], k = 1
# Output: 1
#
#
# Constraints:
#
# 1 <= rows, cols <= 50
# rows == pizza.length
# cols == pizza[i].length
# 1 <= k <= 10
# pizza consists of characters 'A' and '.' only.
from functools import cache
from typing import List


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        R = len(pizza)
        C = len(pizza[0])

        @cache
        def hasApple(startRow, startCol, endRow, endCol):
            for r in range(startRow, endRow + 1):
                for c in range(startCol, endCol + 1):
                    if pizza[r][c] == 'A':
                        return True
            return False

        @cache
        def dp(startRow, startCol, numSlicesLeft):

            if numSlicesLeft == 1:
                if hasApple(startRow, startCol, R - 1, C - 1):
                    return 1
                else:
                    return 0

            numWays = 0
            for i in range(startCol + 1, C):
                if hasApple(startRow, startCol, R - 1, i - 1):
                    numWays += dp(startRow, i, numSlicesLeft - 1)
            for j in range(startRow + 1, R):
                if hasApple(startRow, startCol, j - 1, C - 1):
                    numWays += dp(j, startCol, numSlicesLeft - 1)
            return numWays

        return dp(0, 0, k) % (10 ** 9 + 7)


sol = Solution()
assert sol.ways(["A..","AAA","..."], 3) == 3
assert sol.ways(["A..","AA.","..."], 3) == 1
