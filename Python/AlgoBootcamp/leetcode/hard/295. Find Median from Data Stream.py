# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.
#
# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:
#
# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
# Example 1:
#
# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]
#
# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
# Constraints:
#
# -105 <= num <= 105
# There will be at least one element in the data structure before calling findMedian.
# At most 5 * 104 calls will be made to addNum and findMedian.
#
#
# Follow up:
#
# If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
# If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
from heapq import heappush, heappop


class MedianFinder:

    def __init__(self):
        # heap in py is: 1(Top), 2, 3, 4
        self.left = []  # inverse numbers (to return biggest element)
        self.right = []  # natural order, will return smallest element

    def addNum(self, num: int) -> None:
        if self.right and num > self.right[0]:
            # insert to right
            heappush(self.right, num)
        else:
            # insert to left
            heappush(self.left, -num)

        # normalize size of arrays
        self.normalizeArrays()

    def normalizeArrays(self):
        if abs(len(self.left) - len(self.right)) <= 1:
            return
        if len(self.left) < len(self.right):
            # pop right and push inverse to left
            num = heappop(self.right)
            heappush(self.left, -num)
        elif len(self.left) > len(self.right):
            # pop left and push inverse to right
            num = heappop(self.left)
            heappush(self.right, -num)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        elif len(self.left) < len(self.right):
            return self.right[0]
        else:
            return (-self.left[0] + self.right[0]) / 2


obj = MedianFinder()
obj.addNum(1)
assert obj.findMedian() == 1
obj.addNum(2)
assert obj.findMedian() == 1.5
obj.addNum(5)
assert obj.findMedian() == 2


class MedianFinder2:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        # add item by using a binari search to left or right side
        # bring left/right arrays to equal size
        if self.right and num > self.right[0]:
            # insert to right
            self.addNumToArray(num, self.right)
        else:
            # insert to left
            self.addNumToArray(num, self.left)

        # normalize size of arrays
        self.normalizeArrays()

    def normalizeArrays(self):
        if abs(len(self.left) - len(self.right)) <= 1:
            return
        if len(self.left) < len(self.right):
            self.left.append(self.right[0])
            del self.right[0]
        elif len(self.left) > len(self.right):
            self.right.insert(0, self.left[-1])
            del self.left[-1]

    def addNumToArray(self, num: int, arr) -> None:
        if len(arr) == 0:
            arr.append(num)
            return

        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == num:
                arr.insert(mid, num)
                return
            elif arr[mid] > num:
                r = mid - 1
            else:
                l = mid + 1
        # [1R, 3L, 5] 2
        arr.insert(l, num)

        # [1, 3R, 5L] 4
        # arr.insert(l, num)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return self.left[-1]
        elif len(self.left) < len(self.right):
            return self.right[0]
        else:
            return (self.left[-1] + self.right[0]) / 2


obj = MedianFinder2()
obj.addNum(1)
assert obj.findMedian() == 1
obj.addNum(2)
assert obj.findMedian() == 1.5
obj.addNum(5)
assert obj.findMedian() == 2
