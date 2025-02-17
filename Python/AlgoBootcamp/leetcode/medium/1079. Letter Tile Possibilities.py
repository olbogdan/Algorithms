# You have n  tiles, where each tile has one letter tiles[i] printed on it.
#
# Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.
#
#
#
# Example 1:
#
# Input: tiles = "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
# Example 2:
#
# Input: tiles = "AAABBC"
# Output: 188
# Example 3:
#
# Input: tiles = "V"
# Output: 1
#
#
# Constraints:
#
# 1 <= tiles.length <= 7
# tiles consists of uppercase English letters.


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        result = set()
        usedIdx = [False] * len(tiles)
        def simulate(runStr):
            result.add(runStr)
            result.add(runStr[::-1])
            for i in range(len(tiles)):
                if usedIdx[i] is False:
                    usedIdx[i] = True
                    simulate(runStr + tiles[i])
                    usedIdx[i] = False

        # starting points
        for i in range(len(tiles)):
            usedIdx[i] = True
            simulate(tiles[i])
            usedIdx[i] = False
        return len(result)


sol = Solution()
assert sol.numTilePossibilities("AAB") == 8
assert sol.numTilePossibilities("AAABBC") == 188
