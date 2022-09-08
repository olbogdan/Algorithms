# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

def longestConsecutive(nums: [int]) -> int:
    if len(nums) == 0:
        return 0
    collection = set(nums)

    result = 1

    for i in nums:
        # detect start of a sequence
        if i - 1 not in collection:
            # found start of a sequence
            tempresult = 0
            sequenceI = i
            while sequenceI in collection:
                tempresult += 1
                sequenceI += 1
            result = max(result, tempresult)

    return result


assert longestConsecutive([0,1,2,4,8,5,6,7,9,3,55,88,77,99,999999999]) == 10
assert longestConsecutive([100,4,200,1,3,2]) == 4