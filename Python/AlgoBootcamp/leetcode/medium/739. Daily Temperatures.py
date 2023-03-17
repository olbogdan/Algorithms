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


# O(n)
def dailyTemperatures(temperatures: List[int]) -> List[int]:
    result = [0] * len(temperatures)
    stack = []  # keep indexes, of values in stack decreasing order

    for index, temperature in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temperature:
            prevIdx = stack.pop()
            result[prevIdx] = index - prevIdx
        stack.append(index)
    return result


assert dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
assert dailyTemperatures([30,40,50,60]) == [1,1,1,0]
assert dailyTemperatures([30,60,90]) == [1,1,0]


def dailyTemperatures2(temperatures: List[int]) -> List[int]:
    lenght = len(temperatures)
    result = [0] * lenght

    # iterate from the last day back to the first day
    for index in range(lenght - 1, -1, -1):
        nextDay = index + 1
        while nextDay < lenght:
            # next day temp is higher than current
            # so next warm day is found by index `nextDay`
            if temperatures[nextDay] > temperatures[index]:
                result[index] = nextDay - index
                break
            # next day temp is lover or equals to current day
            # also next day has recorded value 0 means no warmest day in feature was found
            elif result[nextDay] == 0:
                break
            # next day is lover then current but has a record of a day that warmest then nextDay in feature
            else:
                nextDay += result[nextDay]
    return result


assert dailyTemperatures2([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
assert dailyTemperatures2([30,40,50,60]) == [1,1,1,0]
assert dailyTemperatures2([30,60,90]) == [1,1,0]


def dailyTemperatures3(temperatures: List[int]) -> List[int]:
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


assert dailyTemperatures3([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
assert dailyTemperatures3([30,40,50,60]) == [1,1,1,0]
assert dailyTemperatures3([30,60,90]) == [1,1,0]


def dailyTemperatures4(temperatures: List[int]) -> List[int]:
    res = [0] * len(temperatures)
    stack = []  # pair: [temp, index]

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            res[stackInd] = i - stackInd
        stack.append((t, i))
    return res


assert dailyTemperatures4([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
assert dailyTemperatures4([30,40,50,60]) == [1,1,1,0]
assert dailyTemperatures4([30,60,90]) == [1,1,0]