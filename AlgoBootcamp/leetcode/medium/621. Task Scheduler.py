# Given a characters array tasks,
# representing the tasks a CPU
# needs to do, where each letter represents a different task.
# Tasks could be done in any order. Each task is done in one
# unit of time. For each unit of time, the CPU could complete
# either one task or just be idle.
#
# However, there is a non-negative integer
# n that represents the cooldown period between
# two same tasks (the same letter in the array),
# that is that there must be at least n units of time between any two same tasks.
#
# Return the least number of units of times
# that the CPU will take to finish all the given tasks.
# Example 1:
#
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation:
# A -> B -> idle -> A -> B -> idle -> A -> B
# There is at least 2 units of time between any two same tasks.
# Example 2:
#
# Input: tasks = ["A","A","A","B","B","B"], n = 0
# Output: 6
# Explanation: On this case any permutation of size 6 would work since n = 0.
# ["A","A","A","B","B","B"]
# ["A","B","A","B","A","B"]
# ["B","B","B","A","A","A"]
# ...
# And so on.
# Example 3:
#
# Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
# Output: 16
# Explanation:
# One possible solution is
# A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
#
#
# Constraints:
#
# 1 <= task.length <= 104
# tasks[i] is upper-case English letter.
# The integer n is in the range [0, 100].
from collections import Counter, deque
from heapq import heappush, heappop, heapify
from typing import List


# O(n * m) idleTime * tasks
class Solution1:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        countTasksMap = {}
        for t in tasks:
            if t in countTasksMap:
                countTasksMap[t] = countTasksMap[t] + 1
            else:
                countTasksMap[t] = 1

        countTasksHeap = []
        # we don't care about names of tasks here,
        # add a count of reps of each task to array
        for count in countTasksMap.values():
            # python has a max heap, to make a min heap multiply a val by -1
            countTasksHeap.append(count * -1)

        heapify(countTasksHeap)

        cooldownQueue = []

        result = 0
        while countTasksHeap or cooldownQueue:
            if countTasksHeap:
                # take a tasks with most repeats from a heap
                task = heappop(countTasksHeap)
                task += 1
                if task != 0:
                    # add a [number of task repeats numbers : task available time unit]
                    cooldownQueue.append([task, result + n])

            # take task from a queue if [task available time unit] == current result
            if cooldownQueue and cooldownQueue[0][1] == result:
                heappush(countTasksHeap, cooldownQueue[0][0])
                del cooldownQueue[0]
            result += 1
        return result


sol = Solution1()
assert sol.leastInterval(["A","A","A","B","B","B"], 2) == 8
assert sol.leastInterval(["A","A","A","B","B","B"], 0) == 6



class Solution2:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        count = Counter(tasks)

        maxHeap = [-taskReps for taskReps in count.values()]
        heapify(maxHeap)
        taskQueue = deque()
        time = 0
        while maxHeap or taskQueue:

            if maxHeap:
                # take a tasks with most repeats from a heap
                taskReps = heappop(maxHeap)
                # taskReaps is negative, add 1 positive to subtract a number
                taskReps += 1
                # if the task should be run more times add it to a queue
                if taskReps != 0:
                    # add a [number of task repeats numbers : time available again]
                    taskQueue.append([taskReps, time + n])

            # take task from a queue if [task available time unit] == current result
            if taskQueue and taskQueue[0][1] == time:
                heappush(maxHeap, taskQueue.popleft()[0])
            time += 1
        return time


sol = Solution2()
assert sol.leastInterval(["A","A","A","B","B","B"], 2) == 8
assert sol.leastInterval(["A","A","A","B","B","B"], 0) == 6