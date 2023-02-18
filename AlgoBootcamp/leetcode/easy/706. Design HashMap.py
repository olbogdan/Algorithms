# Design a HashMap without using any built-in hash table libraries.
#
# Implement the MyHashMap class:
#
# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
#
#
# Example 1:
#
# Input
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]
#
# Explanation
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // The map is now [[1,1]]
# myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
# myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
# myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
# myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
# myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
# myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
# myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
#
#
# Constraints:
#
# 0 <= key, value <= 106
# At most 104 calls will be made to put, get, and remove.


class Node:
    def __init__(self, key=-1, val=-1, next=None):
        self.val = val
        self.next = next
        self.key = key


class MyHashMap:

    def __init__(self):
        self.arr = [None] * 10000

    def put(self, key: int, value: int) -> None:
        idx = self.getIndexByKey(key)

        if not self.arr[idx]:
            self.arr[idx] = Node(next=Node(key=key, val=value))
        else:
            node = self.arr[idx]
            while node.next and node.next.key != key:
                node = node.next

            if node.next is None:
                node.next = Node(key=key, val=value)
            else:
                node.next.val = value

    def get(self, key: int) -> int:
        idx = self.getIndexByKey(key)
        node = self.arr[idx]
        while node and node.key != key:
            node = node.next
        if node is not None:
            return node.val
        else:
            return -1

    def remove(self, key: int) -> None:
        idx = self.getIndexByKey(key)
        node = self.arr[idx]
        while node and node.next and node.next.key != key:
            node = node.next
        if node and node.next:
            node.next = node.next.next

    def getIndexByKey(self, key: int):
        return key % 10000


obj = MyHashMap()
obj.put(1,1)
param_2 = obj.get(1)
assert param_2 == 1
obj.remove(1)
assert obj.get(1) == -1