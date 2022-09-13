from typing import Optional

# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.

class Node:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next

    def __repr__(self):
        return str(self.data)

def mergeTwoLists(list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
    #         create a dummy node
    #         do iterate while both list not null
    #         add a smaller item to a result list
    #         add all leftovers from a longer list
    dummyNode = Node()
    currentNode = dummyNode
    head1 = list1
    head2 = list2

    while head1 and head2:
        if head1.data <= head2.data:
            currentNode.next = head1
            head1 = head1.next
        else:
            currentNode.next = head2
            head2 = head2.next
        currentNode = currentNode.next

    if head1:
        currentNode.next = head1
    if head2:
        currentNode.next = head2

    return dummyNode.next


n4 = Node(4, None)
n3 = Node(3, n4)
n2 = Node(1, n3)
n1 = Node(1, n2)
sn2 = Node(12, None)
sn1 = Node(0, sn2)

result = mergeTwoLists(n1, sn1)
assert result.data == 0
assert result.next.data == 1
assert result.next.next.data == 1
assert result.next.next.next.data == 3
assert result.next.next.next.next.data == 4
assert result.next.next.next.next.next.data == 12


def mergeTwoLists2(list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
    resultNode = Node(-1, None)
    current = resultNode
    while list1 and list2:
        if list1.data < list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    if list1:
        current.next = list1
    if list2:
        current.next = list2

    return resultNode.next


n4 = Node(4, None)
n3 = Node(3, n4)
n2 = Node(1, n3)
n1 = Node(1, n2)
sn2 = Node(12, None)
sn1 = Node(0, sn2)

result = mergeTwoLists2(n1, sn1)
assert result.data == 0
assert result.next.data == 1
assert result.next.next.data == 1
assert result.next.next.next.data == 3
assert result.next.next.next.next.data == 4
assert result.next.next.next.next.next.data == 12