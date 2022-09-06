# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# O(nlogn)
def topKFrequent(nums: [int], k: int) -> [int]:
    hashmap = {}
    for i in nums:
        hashmap[i] = hashmap.get(i, 0) + 1

    list = [] * len(hashmap)
    for i in hashmap:
        list.append([i, hashmap[i]])

    list.sort(key=lambda x: x[1])

    result = []
    for i in range(k):
        r = list.pop()
        result.append(r[0])

    return result


assert topKFrequent([1,1,1,2,2,3], 2) == [1,2]
assert topKFrequent([-1, -1], 1) == [-1]