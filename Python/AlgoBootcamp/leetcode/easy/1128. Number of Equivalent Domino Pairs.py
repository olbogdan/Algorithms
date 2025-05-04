# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.
#
# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].
#
#
#
# Example 1:
#
# Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1
# Example 2:
#
# Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
# Output: 3
#
#
# Constraints:
#
# 1 <= dominoes.length <= 4 * 104
# dominoes[i].length == 2
# 1 <= dominoes[i][j] <= 9
from collections import defaultdict
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = defaultdict(int)
        for a, b in dominoes:
            if (a, b) in count:
                count[(a, b)] += 1
            else:
                count[(b, a)] += 1
        res = 0
        for val in count.values():
            res += (val * (val-1)) // 2
        return res


sol = Solution()
assert sol.numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6]]) == 1
assert sol.numEquivDominoPairs([[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]) == 3
