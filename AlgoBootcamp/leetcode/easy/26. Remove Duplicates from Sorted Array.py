def removeDuplicates(nums: [int]) -> int:
    filteredSize = 0
    for i in range(0, len(nums)):
        current = nums[i]
        lastSorted = nums[filteredSize]
        if current != lastSorted:
            filteredSize += 1
            nums[i], nums[filteredSize] = lastSorted, current

    filteredSize += 1
    return filteredSize

assert removeDuplicates([1,1,2,4,4]) == 3
assert removeDuplicates([1,1,2]) == 2
assert removeDuplicates([1,1,1]) == 1
