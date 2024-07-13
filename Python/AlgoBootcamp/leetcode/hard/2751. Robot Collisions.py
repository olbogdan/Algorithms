# There are n 1-indexed robots, each having a position on a line, health, and movement direction.
#
# You are given 0-indexed integer arrays positions, healths, and a string directions (directions[i] is either 'L' for left or 'R' for right). All integers in positions are unique.
#
# All robots start moving on the line simultaneously at the same speed in their given directions. If two robots ever share the same position while moving, they will collide.
#
# If two robots collide, the robot with lower health is removed from the line, and the health of the other robot decreases by one. The surviving robot continues in the same direction it was going. If both robots have the same health, they are both removed from the line.
#
# Your task is to determine the health of the robots that survive the collisions, in the same order that the robots were given, i.e. final heath of robot 1 (if survived), final health of robot 2 (if survived), and so on. If there are no survivors, return an empty array.
#
# Return an array containing the health of the remaining robots (in the order they were given in the input), after no further collisions can occur.
#
# Note: The positions may be unsorted.
#
#
#
#
# Example 1:
#
#
#
# Input: positions = [5,4,3,2,1], healths = [2,17,9,15,10], directions = "RRRRR"
# Output: [2,17,9,15,10]
# Explanation: No collision occurs in this example, since all robots are moving in the same direction. So, the health of the robots in order from the first robot is returned, [2, 17, 9, 15, 10].
# Example 2:
#
#
#
# Input: positions = [3,5,2,6], healths = [10,10,15,12], directions = "RLRL"
# Output: [14]
# Explanation: There are 2 collisions in this example. Firstly, robot 1 and robot 2 will collide, and since both have the same health, they will be removed from the line. Next, robot 3 and robot 4 will collide and since robot 4's health is smaller, it gets removed, and robot 3's health becomes 15 - 1 = 14. Only robot 3 remains, so we return [14].
# Example 3:
#
#
#
# Input: positions = [1,2,5,6], healths = [10,10,11,11], directions = "RLRL"
# Output: []
# Explanation: Robot 1 and robot 2 will collide and since both have the same health, they are both removed. Robot 3 and 4 will collide and since both have the same health, they are both removed. So, we return an empty array, [].
#
#
# Constraints:
#
# 1 <= positions.length == healths.length == directions.length == n <= 105
# 1 <= positions[i], healths[i] <= 109
# directions[i] == 'L' or directions[i] == 'R'
# All values in positions are distinct
from typing import List


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        def createAdj():
            adj = []
            for i in range(len(positions)):
                adj.append((positions[i], healths[i], directions[i]))
            adj.sort()
            return adj

        def simulator(adj) -> List[int]:
            R = 'R'
            L = 'L'
            stack = []
            for pos, health, direction in adj:
                stack.append([pos, health, direction])
                while len(stack) >= 2 and stack[-2][2] == R and stack[-1][2] == L:
                    robotGoRight = stack[-2]
                    robotGoLeft = stack[-1]
                    if robotGoRight[1] - robotGoLeft[1] == 0:
                        # remove both
                        stack.pop()
                        stack.pop()
                    elif robotGoRight[1] > robotGoLeft[1]:
                        stack.pop()  # remove robot go left
                        robotGoRight[1] -= 1
                        if robotGoRight[1] == 0:
                            stack.pop()
                    else:
                        del stack[-2]  # remove robot go right
                        robotGoLeft[1] -= 1
                        if robotGoLeft[1] == 0:
                            stack.pop()
            return stack

        def toMap(survived):
            m = {}
            for pos, health, _ in survived:
                m[pos] = health
            return m

        def result(mappedRobots):
            r = []
            for p in positions:
                if p in mappedRobots:
                    r.append(mappedRobots[p])
            return r

        adj = createAdj()
        survived = simulator(adj)
        mappedRobots = toMap(survived)

        return result(mappedRobots)


s = Solution()
assert s.survivedRobotsHealths([5, 4, 3, 2, 1], [2, 17, 9, 15, 10], "RRRRR") == [2, 17, 9, 15, 10]
assert s.survivedRobotsHealths([3, 5, 2, 6], [10, 10, 15, 12], "RLRL") == [14]
