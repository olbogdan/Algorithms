# Given a linked list, return true if the list is circular, false if not
from AlgoBootcamp.linkedlist.LinkedList import LinkedList

# O(n) solution with O(1) memory,
def circular1(list):
    slow = list.head
    fast = list.head
    while fast and fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False


list = LinkedList()
a = LinkedList.Node("a", None)
b = LinkedList.Node("b", None)
c = LinkedList.Node("c", None)
list.head = a
a.next = b
b.next = c
c.next = b

assert circular1(list) is True

list = LinkedList()
a = LinkedList.Node("a", None)
b = LinkedList.Node("b", None)
list.head = a
a.next = b
b.next = a

assert circular1(list) is True

list = LinkedList()
a = LinkedList.Node("a", None)
b = LinkedList.Node("b", None)
c = LinkedList.Node("c", None)
list.head = a
a.next = b
b.next = c

assert circular1(list) is False

list = LinkedList()
a = LinkedList.Node("a", None)
list.head = a
a.next = a

assert circular1(list) is True

# with additional O(n) memory
def circular2(list):
    visitedNodes = set()
    node = list.head
    while node:
        if node in visitedNodes:
            return True
        visitedNodes.add(node)
        node = node.next
    return False


list = LinkedList()
a = LinkedList.Node("a", None)
b = LinkedList.Node("b", None)
c = LinkedList.Node("c", None)
list.head = a
a.next = b
b.next = c
c.next = b

assert circular2(list) is True

list = LinkedList()
a = LinkedList.Node("a", None)
b = LinkedList.Node("b", None)
list.head = a
a.next = b
b.next = a

assert circular2(list) is True

list = LinkedList()
a = LinkedList.Node("a", None)
b = LinkedList.Node("b", None)
c = LinkedList.Node("c", None)
list.head = a
a.next = b
b.next = c

assert circular2(list) is False

list = LinkedList()
a = LinkedList.Node("a", None)
list.head = a
a.next = a

assert circular2(list) is True
