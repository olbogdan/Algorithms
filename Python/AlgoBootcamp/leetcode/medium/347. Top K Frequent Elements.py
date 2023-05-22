# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
from collections import Counter, defaultdict
from typing import List


# O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numReps = Counter(nums)
        repsToNum = {}
        for num, reps in numReps.items():
            repsToNum.setdefault(reps, []).append(num)

        result = []
        for i in reversed(range(len(nums) + 1)):
            if i in repsToNum:
                for num in repsToNum[i]:
                    if len(result) == k:
                        return result
                    result.append(num)
        return result


sol = Solution()
res = sol.topKFrequent([1], 1)
assert res == [1]
assert sol.topKFrequent([-1, -1], 1) == [-1]


class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numReps = Counter(nums)
        repsToNum = defaultdict(list)
        for num, reps in numReps.items():
            repsToNum[reps].append(num)

        result = []
        for i in reversed(range(len(nums) + 1)):
            for num in repsToNum[i]:
                if len(result) == k:
                    return result
                result.append(num)

        return result


sol = Solution2()
res = sol.topKFrequent([1], 1)
assert res == [1]
assert sol.topKFrequent([-1, -1], 1) == [-1]


def topKFrequent(nums: [int], k: int) -> [int]:
    frequent = {}
    for n in nums:
        frequent[n] = frequent.get(n, 0) + 1

    bucket = [[] for i in range(len(nums) + 1)]

    for n in frequent:
        repeats = frequent[n]
        bucket[repeats].append(n)

    result = []
    for i in range(len(bucket) - 1, 0, -1):
        for n in bucket[i]:
            result.append(n)
            if len(result) == k:
                return result

    return result

# O(nlogn)
def topKFrequent2(nums: [int], k: int) -> [int]:
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

assert topKFrequent2([1,1,1,2,2,3], 2) == [1,2]
assert topKFrequent2([-1, -1], 1) == [-1]