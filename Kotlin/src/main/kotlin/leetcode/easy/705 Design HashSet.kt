package leetcode.easy
/*Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.


Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)


Constraints:

0 <= key <= 106
At most 104 calls will be made to add, remove, and contains.*/

class Node(var `val`: Int? = null, var next: Node? = null)

class `705 Design HashSet` {
    private val set = Array<Node>(10001) { Node() }

    fun add(key: Int) {
        val node = set[getHash(key)]
        if (contains(key)) return
        val prevNext = node.next
        node.next = Node(key, prevNext)
    }

    fun remove(key: Int) {
        var node: Node? = set[getHash(key)]
        var prev: Node? = null
        while (node != null) {
            if (node.`val` == key) {
                prev?.next = node.next
                return
            }
            prev = node
            node = node.next
        }
    }

    fun contains(key: Int): Boolean {
        var node = set[getHash(key)].next
        while (node != null) {
            if (node.`val` == key) {
                return true
            }
            node = node.next
        }
        return false
    }

    private fun getHash(key: Int): Int {
        return key % set.size
    }
}


class `705 Design HashSet2` {
    private var size = 10007
    private val loadFactor = 0.75
    private var count = 0
    private var set = Array<Node?>(size) { null }

    fun add(key: Int) {
        if (contains(key)) return
        if (count >= size * loadFactor) resize()
        val index = getHash(key)
        val node = Node(key)
        node.next = set[index]
        set[index] = node
        count++
    }

    fun remove(key: Int) {
        val index = getHash(key)
        val dummy = Node(0)
        dummy.next = set[index]
        var prev: Node? = dummy
        var curr = set[index]
        while (curr != null) {
            if (curr.value == key) {
                prev?.next = curr.next
                set[index] = dummy.next
                count--
                return
            }
            prev = curr
            curr = curr.next
        }
    }

    fun contains(key: Int): Boolean {
        val index = getHash(key)
        var curr = set[index]
        while (curr != null) {
            if (curr.value == key) {
                return true
            }
            curr = curr.next
        }
        return false
    }

    private fun resize() {
        size *= 2 // double the size
        val oldSet = set
        set = Array<Node?>(size) { null } // create a new array with the new size
        count = 0
        for (node in oldSet) {
            var curr = node
            while (curr != null) {
                add(curr.value) // rehash all the elements in the old array
                curr = curr.next
            }
        }
    }

    private fun getHash(key: Int): Int {
        return key % size
    }

    private class Node(val value: Int, var next: Node? = null)
}



/**
 * Your MyHashSet object will be instantiated and called as such:
 * var obj = MyHashSet()
 * obj.add(key)
 * obj.remove(key)
 * var param_3 = obj.contains(key)
 */