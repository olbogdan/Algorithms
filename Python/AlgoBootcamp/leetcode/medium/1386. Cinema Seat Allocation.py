# A cinema has n rows of seats, numbered from 1 to n. Each row has 10 seats, numbered from 1 to 10.
#
# You are given a 2D integer array reservedSeats, where reservedSeats[i] = [rowi, seati] means that seat seati in row rowi is already reserved.
#
# A four-person group must be assigned to four seats in the same row. The group can be seated in one of the following seat blocks:
#
# seats 2, 3, 4, 5
# seats 4, 5, 6, 7
# seats 6, 7, 8, 9
# A block can be used only if none of its seats are reserved. Each seat can be assigned to at most one group.
#
# Return an integer denoting the maximum number of four-person groups that can be assigned.
#
#
#
# Example 1:
#
#
#
# Input: n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
# Output: 4
# Explanation: The figure above shows an optimal allocation of four groups. Seats marked in blue are already reserved, and each set of four contiguous seats marked in orange is assigned to one group.
# Example 2:
#
# Input: n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
# Output: 2
# Example 3:
#
# Input: n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
# Output: 4
#
#
# Constraints:
#
# 1 <= n <= 109
# 1 <= reservedSeats.length <= min(10 * n, 104)
# reservedSeats[i] == [rowi, seati]
# 1 <= rowi <= n
# 1 <= seati <= 10
# All reservedSeats[i] are distinct.
from collections import defaultdict
from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
            adj = defaultdict(list)
            for r, c in reservedSeats:
                adj[r-1].append(c-1)

            res = 0
            for r in range(n):
                firstFree = 1
                for i in range(1, 5):
                    if i in adj[r]:
                        firstFree = 0
                        break
                secondFree = 1
                for i in range(5, 9):
                    if i in adj[r]:
                        secondFree = 0
                        break
                middleFree = 1
                for i in range(3, 7):
                    if i in adj[r]:
                        middleFree = 0
                        break
                res += max(middleFree, firstFree + secondFree)

            return res


sol = Solution()
print(sol.maxNumberOfFamilies(n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]))
# assert sol.maxNumberOfFamilies(n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]) == 3