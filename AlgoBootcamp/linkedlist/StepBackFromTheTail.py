# Given a linked list and integer n, return the element n spaces from the last node in the list
# do not call the size method of the linked list, assume that n will always be less than the length of the list
from AlgoBootcamp.linkedlist.LinkedList import LinkedList


def from_last(list: LinkedList, n):
    slow = list.head
    fast = list.head
    for i in range(n):
        fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next
    return slow.data


list = LinkedList()
list.add_last("a")
list.add_last("b")
list.add_last("c")
list.add_last("d")
list.add_last("e")
list.add_last("f")

assert from_last(list, 5) == "a"
assert from_last(list, 0) == "f"
assert from_last(list, 1) == "e"