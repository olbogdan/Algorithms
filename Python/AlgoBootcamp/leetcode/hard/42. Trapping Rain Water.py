#Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:
#
# Input: height = [4,2,0,3,2,5]
# Output: 9
#
#
# Constraints:
#
# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105
from typing import List


def trap(height: List[int]) -> int:
    trap = 0
    curLeftBorder, curRightBorder = height[0], height[-1]
    l, r = 0, len(height) - 1
    while l < r:
        if curLeftBorder < curRightBorder:
            l += 1
            curLeftBorder = max(curLeftBorder, height[l])
            trap += curLeftBorder - height[l]
        else:
            r -= 1
            curRightBorder = max(curRightBorder, height[r])
            trap += curRightBorder - height[r]
    return trap


assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
assert trap([4,2,0,3,2,5]) == 9
assert trap([1,2,0,1,2,0,1,2,0]) == 6
assert trap([0,3,0]) == 0
assert trap([1,0,1]) == 1


def trap2(height: List[int]) -> int:
    trap = 0
    curMin = 0
    l = 0
    r = len(height) - 1
    while l < r:
        # if current index(height) is lower than borders then count the trapped watter
        # the highest border will never be moved and will produce 0 or negative after curMin deduction
        # so that it is safe to check both  l and r pointers here
        if curMin - height[l] > 0:
            trap += curMin - height[l]
        if curMin - height[r] > 0:
            trap += curMin - height[r]
        # find minimum of l/r border but not less than cur min
        curMin = max(curMin, min(height[l], height[r]))
        # move smallest border
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return trap


assert trap2([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
assert trap2([4,2,0,3,2,5]) == 9
assert trap2([1,2,0,1,2,0,1,2,0]) == 6
assert trap2([0,3,0]) == 0
assert trap2([1,0,1]) == 1
