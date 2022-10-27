# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
# Implement the LRUCache class:
#
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists.
# Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation,
# evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.
#
# Example 1:
#
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
#
#
# Constraints:
#
# 1 <= capacity <= 3000
# 0 <= key <= 104
# 0 <= value <= 105
# At most 2 * 105 calls will be made to get and put.


# 1532 ms faster than 78.34% of Python3 online submissions for LRU Cache.
class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUCache:
    # need a hash map [key, node]
    # need a node class or just a touple of 3 items ([k, v], [k, v], [k, v])
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}  # {key:node}
        self.lastNode = Node(0, 0)  # 0Node -> 1Node -> lastNode (last used node)
        self.oldestNode = Node(0, 0)
        self.oldestNode.next = self.lastNode
        self.lastNode.prev = self.oldestNode

    def get(self, key: int) -> int:
        if key in self.dict:
            # make the node as a last used, update prev and next nodes of the used node
            node = self.dict[key]
            self.markAsLastUsed(node)
            return node.val
        else:
            return -1

    def insertNew(self, node: Node):
        prev, next = self.lastNode.prev, self.lastNode
        prev.next = next.prev = node
        node.next, node.prev = next, prev

    def markAsLastUsed(self, node: Node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        self.insertNew(node)

    def removeOldest(self):
        del self.dict[self.oldestNode.next.key]
        newOldest = self.oldestNode.next.next
        self.oldestNode.next = newOldest
        newOldest.prev = self.oldestNode

    def put(self, key: int, value: int) -> None:
        if key not in self.dict:
            self.dict[key] = Node(key, value)
            self.insertNew(self.dict[key])
        else:
            self.dict[key].val = value
            self.markAsLastUsed(self.dict[key])
        if len(self.dict) > self.capacity:
            self.removeOldest()


obj = LRUCache(3)
obj.put(2,2)
obj.put(3,3)
obj.put(4,4)
# #
param_1 = obj.get(4)
assert param_1 == 4
param_1 = obj.get(3)
assert param_1 == 3
param_1 = obj.get(2)
assert param_1 == 2
obj.put(5,5)
param_1 = obj.get(5)
assert param_1 == 5
param_1 = obj.get(4)
assert param_1 == -1