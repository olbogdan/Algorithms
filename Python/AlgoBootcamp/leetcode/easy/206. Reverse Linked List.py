# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode) -> ListNode:
    prev = None
    current = head
    while current:
        nNode = current.next
        current.next = prev
        prev = current
        current = nNode
    return prev


# Tests
firstNode = ListNode(1, None)
prevNode = firstNode
for i in [2,3,4,5]:
    newNode = ListNode(i, None)
    prevNode.next = newNode
    prevNode = newNode

firstNodeResult = ListNode(5, None)
prevNodeResult = firstNodeResult
for i in [4,3,2,1]:
    newNode = ListNode(i, None)
    prevNodeResult.next = newNode
    prevNodeResult = newNode

testNode = reverseList(firstNode)
while testNode:
    assert firstNodeResult.val == testNode.val
    testNode = testNode.next
    firstNodeResult = firstNodeResult.next



