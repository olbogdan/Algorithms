# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.
#
# Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.
#
#
#
# Example 1:
#
#
# Input: path = "NES"
# Output: false
# Explanation: Notice that the path doesn't cross any point more than once.
# Example 2:
#
#
# Input: path = "NESWW"
# Output: true
# Explanation: Notice that the path visits the origin twice.
#
#
# Constraints:
#
# 1 <= path.length <= 104
# path[i] is either 'N', 'S', 'E', or 'W'.


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        N = 'N'
        S = 'S'
        E = 'E'
        W = 'W'
        visited = set()
        start = (0, 0)
        visited.add(start)
        for c in path:
            if c == N:
                start = (start[0], start[1] + 1)
            elif c == S:
                start = (start[0], start[1] - 1)
            elif c == E:
                start = (start[0] + 1, start[1])
            elif c == W:
                start = (start[0] - 1, start[1])
            if start in visited:
                return True
            visited.add(start)
        return False


assert Solution().isPathCrossing("NESWW") is True
