# Design a number container system that can do the following:
#
# Insert or Replace a number at the given index in the system.
# Return the smallest index for the given number in the system.
# Implement the NumberContainers class:
#
# NumberContainers() Initializes the number container system.
# void change(int index, int number) Fills the container at index with the number. If there is already a number at that index, replace it.
# int find(int number) Returns the smallest index for the given number, or -1 if there is no index that is filled by number in the system.
#
#
# Example 1:
#
# Input
# ["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"]
# [[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]
# Output
# [null, -1, null, null, null, null, 1, null, 2]
#
# Explanation
# NumberContainers nc = new NumberContainers();
# nc.find(10); // There is no index that is filled with number 10. Therefore, we return -1.
# nc.change(2, 10); // Your container at index 2 will be filled with number 10.
# nc.change(1, 10); // Your container at index 1 will be filled with number 10.
# nc.change(3, 10); // Your container at index 3 will be filled with number 10.
# nc.change(5, 10); // Your container at index 5 will be filled with number 10.
# nc.find(10); // Number 10 is at the indices 1, 2, 3, and 5. Since the smallest index that is filled with 10 is 1, we return 1.
# nc.change(1, 20); // Your container at index 1 will be filled with number 20. Note that index 1 was filled with 10 and then replaced with 20.
# nc.find(10); // Number 10 is at the indices 2, 3, and 5. The smallest index that is filled with 10 is 2. Therefore, we return 2.
#
#
# Constraints:
#
# 1 <= index, number <= 109
# At most 105 calls will be made in total to change and find.
from collections import defaultdict
from heapq import heappush, heappop


class NumberContainers:

    def __init__(self):
        self.idxToNum = {} # idx : num (1 : 1)
        self.numToIdxs = defaultdict(list) # num : idexes (1 : many - PQ)

    def change(self, index: int, number: int) -> None:
        # we will not remove the num to indexes,
        # self.numToIdxs can have a link to an index that does not
        # belong to the number, but it is ok, the idxToNum is source of trueth
        if index not in self.idxToNum or self.idxToNum[index] != number:
            self.idxToNum[index] = number
            heappush(self.numToIdxs[number], index)


    def find(self, number: int) -> int:
        # find smallest in the list
        while number in self.numToIdxs and self.numToIdxs[number]:
            idx = self.numToIdxs[number][0]
            if idx in self.idxToNum and self.idxToNum[idx] == number:
                return idx
            # handle the case when idx was reasigned by some other number
            # remove invalid num:idx pair form the PQ
            heappop(self.numToIdxs[number])
        return -1


obj = NumberContainers()
obj.change(2, 10)
obj.change(1, 10)
obj.change(3, 10)
obj.change(5, 10)
assert obj.find(10) == 1
