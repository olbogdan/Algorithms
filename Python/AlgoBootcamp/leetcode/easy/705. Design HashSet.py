# Design a HashSet without using any built-in hash table libraries.
#
# Implement MyHashSet class:
#
# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or not.
# void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
#
#
# Example 1:
#
# Input
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# Output
# [null, null, null, true, false, null, true, null, false]
#
# Explanation
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // return True
# myHashSet.contains(3); // return False, (not found)
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // return True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // return False, (already removed)
#
#
# Constraints:
#
# 0 <= key <= 106
# At most 104 calls will be made to add, remove, and contains.


class Node:

    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class MyHashSet:

    def __init__(self):
        self.set = [Node() for _ in range(10 ** 4 + 1)]

    def add(self, key: int) -> None:
        node = self.set[self.getHash(key)]
        if self.contains(key):
            return
        node = self.set[self.getHash(key)]
        prevNext = node.next
        node.next = Node(key, prevNext)

    def remove(self, key: int) -> None:
        node = self.set[self.getHash(key)]
        prev = None
        while node:
            if node.val == key:
                prev.next = node.next
                break
            prev = node
            node = node.next

    def contains(self, key: int) -> bool:
        node = self.set[self.getHash(key)]
        while node:
            if node.val == key:
                return True
            node = node.next
        return False

    def getHash(self, key: int) -> int:
        return key % len(self.set)

# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(2)
obj.add(2)
assert obj.contains(2) is True
obj.remove(2)
assert obj.contains(2) is False
