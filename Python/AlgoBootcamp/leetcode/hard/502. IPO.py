# Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.
#
# You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.
#
# Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.
#
# Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.
#
# The answer is guaranteed to fit in a 32-bit signed integer.
#
#
#
# Example 1:
#
# Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
# Output: 4
# Explanation: Since your initial capital is 0, you can only start the project indexed 0.
# After finishing it you will obtain profit 1 and your capital becomes 1.
# With capital 1, you can either start the project indexed 1 or the project indexed 2.
# Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
# Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
# Example 2:
#
# Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
# Output: 6
#
#
# Constraints:
#
# 1 <= k <= 105
# 0 <= w <= 109
# n == profits.length
# n == capital.length
# 1 <= n <= 105
# 0 <= profits[i] <= 104
# 0 <= capital[i] <= 109
from heapq import heappush, heappop, heapify
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projectCosts = []
        for i in range(len(capital)):
            projectCosts.append((capital[i], i))
        heapify(projectCosts)

        availableProjects = []

        def updateAvailability():
            while projectCosts and projectCosts[0][0] <= w: # mistakes: don't forget that it is 2 dimen array
                _, i = heappop(projectCosts)
                heappush(availableProjects, -profits[i])

        updateAvailability() # mistakes: don't forget to call before interation
        while availableProjects and k > 0: # mistakes: don't forget check if array is not empty
            w += (-heappop(availableProjects))
            updateAvailability()
            k -= 1

        return w


sol = Solution()
assert sol.findMaximizedCapital(1, 0, [1,2,3], [1,1,2]) == 0
assert sol.findMaximizedCapital(3, 0, [1,2,3], [0,1,2]) == 6


class Solution2:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxHeap = []
        # heapify sort based on capital price, cheaper tasks at the begining
        # (0{price}, 3{earn if take it}), (3, 5), (4, 22)
        # 1 step we have 0 w, take (0,3) will give as 3w
        # 2 step we have 3 w, take (3,5) will cost 3 and will give as 5w
        # 3 step we have 5 w, take (4, 22) will cost 4, and add 22 -
        # as result (5{we had}-4{cost of 3rd step}) + 22 = 23
        minHeap = [ (c, p) for c, p in zip(capital, profits) ]
        heapify(minHeap)
        for _ in range(k):
            while minHeap and minHeap[0][0] <= w:
                _, p = heappop(minHeap)
                heappush(maxHeap, p * -1)
            if not maxHeap:
                break
            w += heappop(maxHeap) * -1

        return w


sol = Solution2()
assert sol.findMaximizedCapital(1, 0, [1,2,3], [1,1,2]) == 0
assert sol.findMaximizedCapital(3, 0, [1,2,3], [0,1,2]) == 6
