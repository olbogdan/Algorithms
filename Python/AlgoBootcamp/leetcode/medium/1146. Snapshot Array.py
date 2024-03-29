# Implement a SnapshotArray that supports the following interface:
#
# SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
# void set(index, val) sets the element at the given index to be equal to val.
# int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
# int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
#
#
# Example 1:
#
# Input: ["SnapshotArray","set","snap","set","get"]
# [[3],[0,5],[],[0,6],[0,0]]
# Output: [null,null,0,null,5]
# Explanation:
# SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
# snapshotArr.set(0,5);  // Set array[0] = 5
# snapshotArr.snap();  // Take a snapshot, return snap_id = 0
# snapshotArr.set(0,6);
# snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
#
#
# Constraints:
#
# 1 <= length <= 5 * 104
# 0 <= index < length
# 0 <= val <= 109
# 0 <= snap_id < (the total number of times we call snap())
# At most 5 * 104 calls will be made to set, snap, and get.


class SnapshotArray:

    def __init__(self, length: int):
        self.arrayMap = {}  # { key=index to val={ key:snep to val=value } }
        self.snepId = 0

    def set(self, index: int, val: int) -> None:
        if index not in self.arrayMap:
            self.arrayMap[index] = {}
        self.arrayMap[index][self.snepId] = val

    def snap(self) -> int:
        self.snepId += 1
        return self.snepId - 1

    def get(self, index: int, snap_id: int) -> int:
        if index not in self.arrayMap:
            return 0
        elif snap_id in self.arrayMap[index]:
            return self.arrayMap[index][snap_id]
        else:
            candidate = 0
            biggestInRangeSnepId = 0
            for key, value in self.arrayMap[index].items():
                if key > biggestInRangeSnepId and key < snap_id:
                    biggestInRangeSnepId = key
                    candidate = value
            return candidate

# Your SnapshotArray object will be instantiated and called as such:
obj = SnapshotArray(1)
param_2 = obj.snap()
obj.set(0, 22)
param_3 = obj.get(0, 0)
assert param_3 == 0
param_3 = obj.get(0, 1)
assert param_3 == 22
