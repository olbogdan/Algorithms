# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#
# Merge all the linked-lists into one sorted linked-list and return it.
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
from collections import Counter
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    counter = Counter()

    for list in lists:
        while list:
            counter[list.val] += 1
            list = list.next

    dummy = ListNode(0, None)
    tail = dummy
    for key in sorted(counter.keys()):
        while counter[key] > 0:
            tail.next = ListNode(key)
            tail = tail.next
            counter[key] -= 1
    return dummy.next


list1 = ListNode(5, ListNode(10, ListNode(20)))
list2 = ListNode(1, ListNode(30, ListNode(40)))
result = mergeKLists([list1, list2])
assert result.val == 1
assert result.next.val == 5
assert result.next.next.val == 10
assert result.next.next.next.val == 20
assert result.next.next.next.next.val == 30
assert result.next.next.next.next.next.val == 40