# You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi] means the ith flower will be in full bloom from starti to endi (inclusive). You are also given a 0-indexed integer array persons of size n, where persons[i] is the time that the ith person will arrive to see the flowers.
#
# Return an integer array answer of size n, where answer[i] is the number of flowers that are in full bloom when the ith person arrives.
#
#
#
# Example 1:
#
#
# Input: flowers = [[1,6],[3,7],[9,12],[4,13]], persons = [2,3,7,11]
# Output: [1,2,2,2]
# Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
# For each person, we return the number of flowers in full bloom during their arrival.
# Example 2:
#
#
# Input: flowers = [[1,10],[3,3]], persons = [3,3,2]
# Output: [2,2,1]
# Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
# For each person, we return the number of flowers in full bloom during their arrival.
#
#
# Constraints:
#
# 1 <= flowers.length <= 5 * 104
# flowers[i].length == 2
# 1 <= starti <= endi <= 109
# 1 <= persons.length <= 5 * 104
# 1 <= persons[i] <= 109
from collections import defaultdict
from typing import List


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        # build a sparsearray
        # sort persons by keepeing original index
        # compute a prefix sum of sparsearray
        # add answers to res on the fly
        spr = defaultdict(int)
        for start, end in flowers:
            spr[start] += 1
            spr[end+1] -= 1
        queries = []
        for idx, person in enumerate(persons):
            queries.append((person, idx))
        queries.sort()
        queriI = 0
        result = [0]*len(persons)
        prefixSum = 0
        keys = sorted(list(spr.keys()))
        for k in keys:
            # when k is in feature time then query, add last valid count to res
            while queriI < len(queries) and queries[queriI][0] < k:
                result[queries[queriI][1]] = prefixSum
                queriI += 1
            # update a current count according to new k
            prefixSum += spr[k]
        return result


sol = Solution()
res = sol.fullBloomFlowers([[1,10],[3,3]], [3])
assert res == [2]
