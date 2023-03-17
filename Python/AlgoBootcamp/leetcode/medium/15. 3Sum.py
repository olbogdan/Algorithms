# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# O(n*n)


def threeSum(nums: [int]) -> [[int]]:
    if len(nums) == 3:
        if sum(nums) == 0:
            return [nums]
        else:
            return []

    nums.sort()
    result = []

    for i in range(0, len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l = i + 1
        r = len(nums) - 1
        while l < r:
            threeSum = nums[i] + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                result.append([nums[i], nums[l], nums[r]])
                l += 1
                while nums[l - 1] == nums[l] and l < r:
                    l += 1

    return result


assert threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
assert threeSum([3,0,-2,-1,1,2]) == [[-2,-1,3],[-2,0,2],[-1,0,1]]
assert threeSum([0,0,0]) == [[0,0,0]]


