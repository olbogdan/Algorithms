# Return the middle node of a linked list.
# If the list has an even number, return the node at the end of first half.


# solutio1: two pointer manipulation, second pointer increments with double speed of a slow one until reaches None.
from AlgoBootcamp.linkedlist.LinkedList import LinkedList


def midpoint1(list):
    slow = list.get_first_node()
    fast = list.get_first_node()
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


list = LinkedList()
list.add_last("a")
list.add_last("b")
list.add_last("c")
list.add_last("d")
list.add_last("e")
result = midpoint1(list).data
assert result == "c"

list = LinkedList()
list.add_last("a")
list.add_last("b")
list.add_last("c")
list.add_last("d")
result = midpoint1(list).data
assert result == "b"

list = LinkedList()
list.add_last("a")
result = midpoint1(list).data
assert result == "a"

list = LinkedList()
result = midpoint1(list)
assert result is None



def midpoint2(list):
    first = list.get_first()
    last = list.get_last()
    while first and last and first != last:
        list.remove_last()
        last = list.get_last()
        if first == last:
            return first
        else:
            list.remove_first()
            first = list.get_first()
    return first



list = LinkedList()
list.add_last("a")
list.add_last("b")
list.add_last("c")
list.add_last("d")
list.add_last("e")
result = midpoint2(list)
assert result == "c"

list = LinkedList()
list.add_last("a")
list.add_last("b")
list.add_last("c")
list.add_last("d")
result = midpoint2(list)
assert result == "b"

list = LinkedList()
list.add_last("a")
result = midpoint2(list)
assert result == "a"

list = LinkedList()
result = midpoint2(list)
assert result is None