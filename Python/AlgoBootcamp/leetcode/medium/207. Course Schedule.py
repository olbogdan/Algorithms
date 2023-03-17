# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
#
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
#
#
#
# Example 1:
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:
#
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
#
#
# Constraints:
#
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.
from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = defaultdict(set)
        for cours, pre in prerequisites:
            prereqMap[cours].add(pre)

        visitedItems = set()

        def canBeFinished(toVisit):
            if toVisit in visitedItems:
                return False
            # toVisit has no prerequisites, success base case
            if toVisit not in prereqMap:
                return True

            visitedItems.add(toVisit)
            requiredCourses = prereqMap[toVisit]
            for rC in requiredCourses:
                if not canBeFinished(rC):
                    return False
            del prereqMap[toVisit]
            visitedItems.remove(toVisit)
            return True

        for num in range(numCourses):
            if not canBeFinished(num):
                return False
        return True


sol = Solution()
res = sol.canFinish(3, [[1,0],[1,2],[0,1]])
assert res == False
res = sol.canFinish(2, [[1,0],[0,1]])
assert res == False
res = sol.canFinish(2, [[1,0]])
assert res == True
res = sol.canFinish(7, [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]])
assert res == True
res = sol.canFinish(8, [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]])
assert res == True