# We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.
#
# Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.
#
#
#
# Example 1:
#
# Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: The first group has [1,4], and the second group has [2,3].
# Example 2:
#
# Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false
# Explanation: We need at least 3 groups to divide them. We cannot put them in two groups.
#
#
# Constraints:
#
# 1 <= n <= 2000
# 0 <= dislikes.length <= 104
# dislikes[i].length == 2
# 1 <= ai < bi <= n
# All the pairs of dislikes are unique.
from collections import defaultdict, deque
from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # crate adj list a to b and b to a
        # crate an array withe/black group
        # iterate bfs on each item, each leverl of bfs has different color
        adj = defaultdict(list)
        for a, b in dislikes:
            adj[a].append(b)
            adj[b].append(a)

        # 0 -> unvisited, 1 -> white, -1 -> black
        whiteBack = [0] * (n + 1)

        # returns false if Bipartition is not possible
        def bfs(i) -> bool:
            if whiteBack[i]:
                return True

            q = deque([i])
            whiteBack[i] = -1
            while q:
                node = q.popleft()
                curColor = whiteBack[node]
                for nei in adj[node]:
                    # neighbors are not alowd to be the same color
                    if whiteBack[nei] == curColor:
                        return False
                    # colorise unvisited
                    elif whiteBack[nei] == 0:
                        q.append(nei)
                        whiteBack[nei] = curColor * -1
                    # visited of inverse color is ignored (except)
            return True

        for i in range(1, n + 1):
            if not bfs(i):
                return False

        return True


sol = Solution()
res = sol.possibleBipartition(3, [[1,2],[1,3],[2,3]])
assert res is False
res = sol.possibleBipartition(3, [[1,2],[1,3]])
assert res is True
