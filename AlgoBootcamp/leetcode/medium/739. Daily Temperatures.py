# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
# Example 1:
#
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:
#
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:
#
# Input: temperatures = [30,60,90]
# Output: [1,1,0]
#
#
# Constraints:
#
# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100


from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    lenght = len(temperatures)
    result = [0] * lenght

    def dfs(temp, i):
        if i >= lenght:
            return 0
        if temperatures[i] > temp:
            return i
        else:
            if result[i] == 0:
                return 0
            else:
                return dfs(temp, i + result[i])

    for i in range(lenght - 1, -1, -1):
        nextWarmDay = dfs(temperatures[i], i + 1)
        if nextWarmDay != 0:
            result[i] = nextWarmDay - i

    return result


assert dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
assert dailyTemperatures([30,40,50,60]) == [1,1,1,0]
assert dailyTemperatures([30,60,90]) == [1,1,0]