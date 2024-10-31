# There are some robots and factories on the X-axis. You are given an integer array robot where robot[i] is the position of the ith robot. You are also given a 2D integer array factory where factory[j] = [positionj, limitj] indicates that positionj is the position of the jth factory and that the jth factory can repair at most limitj robots.
#
# The positions of each robot are unique. The positions of each factory are also unique. Note that a robot can be in the same position as a factory initially.
#
# All the robots are initially broken; they keep moving in one direction. The direction could be the negative or the positive direction of the X-axis. When a robot reaches a factory that did not reach its limit, the factory repairs the robot, and it stops moving.
#
# At any moment, you can set the initial direction of moving for some robot. Your target is to minimize the total distance traveled by all the robots.
#
# Return the minimum total distance traveled by all the robots. The test cases are generated such that all the robots can be repaired.
#
# Note that
#
# All robots move at the same speed.
# If two robots move in the same direction, they will never collide.
# If two robots move in opposite directions and they meet at some point, they do not collide. They cross each other.
# If a robot passes by a factory that reached its limits, it crosses it as if it does not exist.
# If the robot moved from a position x to a position y, the distance it moved is |y - x|.
#
#
# Example 1:
#
#
# Input: robot = [0,4,6], factory = [[2,2],[6,2]]
# Output: 4
# Explanation: As shown in the figure:
# - The first robot at position 0 moves in the positive direction. It will be repaired at the first factory.
# - The second robot at position 4 moves in the negative direction. It will be repaired at the first factory.
# - The third robot at position 6 will be repaired at the second factory. It does not need to move.
# The limit of the first factory is 2, and it fixed 2 robots.
# The limit of the second factory is 2, and it fixed 1 robot.
# The total distance is |2 - 0| + |2 - 4| + |6 - 6| = 4. It can be shown that we cannot achieve a better total distance than 4.
# Example 2:
#
#
# Input: robot = [1,-1], factory = [[-2,1],[2,1]]
# Output: 2
# Explanation: As shown in the figure:
# - The first robot at position 1 moves in the positive direction. It will be repaired at the second factory.
# - The second robot at position -1 moves in the negative direction. It will be repaired at the first factory.
# The limit of the first factory is 1, and it fixed 1 robot.
# The limit of the second factory is 1, and it fixed 1 robot.
# The total distance is |2 - 1| + |(-2) - (-1)| = 2. It can be shown that we cannot achieve a better total distance than 2.
#
#
# Constraints:
#
# 1 <= robot.length, factory.length <= 100
# factory[j].length == 2
# -109 <= robot[i], positionj <= 109
# 0 <= limitj <= robot.length
# The input will be generated such that it is always possible to repair every robot.
from cmath import inf
from typing import List


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        ROBOT_N = len(robot)
        FACTORY_N = len(factory)
        minI = min(min(robot), min(f for f, c in factory))
        if minI < 0:
            minI *= -1
            for i in range(ROBOT_N):
                robot[i] = robot[i] + minI
            for i in range(FACTORY_N):
                factory[i][0] = factory[i][0] + minI

        factoryMap = {}
        for factoryIdx, factorySpace in factory:
            if factorySpace == 0:
                continue
            factoryMap[factoryIdx] = factorySpace

        robot.sort()
        emptyFactories = set()

        def backtrack(i):
            nonlocal robot
            if i == ROBOT_N:
                return 0
            res = float(inf)
            robotIdx = robot[i]
            for factoryIdx in factoryMap.keys():
                if factoryIdx in emptyFactories:
                    continue
                factoryMap[factoryIdx] -= 1
                if factoryMap[factoryIdx] == 0:
                    emptyFactories.add(factoryIdx)
                res = min(res, abs(factoryIdx - robotIdx) + backtrack(i + 1))
                factoryMap[factoryIdx] += 1
                if factoryIdx in emptyFactories:
                    emptyFactories.remove(factoryIdx)
            return res

        return backtrack(0)


sol = Solution()
print(sol.minimumTotalDistance([789300819,-600989788,529140594,-592135328,-840831288,209726656,-671200998], [[-865262624,6],[-717666169,0],[725929046,2],[449443632,3],[-912630111,0],[270903707,3],[-769206598,2],[-299780916,4],[-159433745,5],[-467185764,3],[849991650,7],[-292158515,6],[940410553,6],[258278787,0],[83034539,2],[54441577,3],[-235385712,2],[75791769,3]]))