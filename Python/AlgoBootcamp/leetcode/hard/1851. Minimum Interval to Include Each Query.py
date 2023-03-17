# You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting at lefti and ending at righti (inclusive). The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.
#
# You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i such that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.
#
# Return an array containing the answers to the queries.
#
#
#
# Example 1:
#
# Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
# Output: [3,3,1,4]
# Explanation: The queries are processed as follows:
# - Query = 2: The interval [2,4] is the smallest interval containing 2. The answer is 4 - 2 + 1 = 3.
# - Query = 3: The interval [2,4] is the smallest interval containing 3. The answer is 4 - 2 + 1 = 3.
# - Query = 4: The interval [4,4] is the smallest interval containing 4. The answer is 4 - 4 + 1 = 1.
# - Query = 5: The interval [3,6] is the smallest interval containing 5. The answer is 6 - 3 + 1 = 4.
# Example 2:
#
# Input: intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
# Output: [2,-1,4,6]
# Explanation: The queries are processed as follows:
# - Query = 2: The interval [2,3] is the smallest interval containing 2. The answer is 3 - 2 + 1 = 2.
# - Query = 19: None of the intervals contain 19. The answer is -1.
# - Query = 5: The interval [2,5] is the smallest interval containing 5. The answer is 5 - 2 + 1 = 4.
# - Query = 22: The interval [20,25] is the smallest interval containing 22. The answer is 25 - 20 + 1 = 6.
#
#
# Constraints:
#
# 1 <= intervals.length <= 105
# 1 <= queries.length <= 105
# intervals[i].length == 2
# 1 <= lefti <= righti <= 107
# 1 <= queries[j] <= 107
from heapq import heappop, heappush
from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # heap with (size, right)
        # sorted intervals
        # sorted queries with keeping an original index
        queriesX = []
        for idx, val in enumerate(queries):
            queriesX.append((val, idx))
        queriesX.sort()

        intervals.sort()
        res = [-1]*len(queries)
        h = [] # heap with (size, right border)
        intervalIdx = 0
        for val, idx in queriesX:
            # right < curQuery, remove outdated intervals
            while h and h[0][1] < val:
                heappop(h)
            while intervalIdx < len(intervals) and val >= intervals[intervalIdx][0]:
                if val <= intervals[intervalIdx][1]:
                    right = intervals[intervalIdx][1]
                    size = right - intervals[intervalIdx][0] + 1
                    heappush(h, (size, right))
                intervalIdx += 1
            if h:
                size = h[0][0]
                res[idx] = size
        return res


sol = Solution()
res = sol.minInterval([[4,5],[5,8],[1,9],[8,10],[1,6]], [7,9,3,9,3])
print(res)
# [4,3,6,3,6]
# [9,9,6,9,6]