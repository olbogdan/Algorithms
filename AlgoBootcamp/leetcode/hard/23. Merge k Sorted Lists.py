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
from heapq import heappush, heappop
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

def mergeKListsHeap(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []
    for list in lists:
        while list:
            heappush(heap, list.val)
            list = list.next
    dummy = tail = ListNode()
    while heap:
        tail.next = ListNode(heappop(heap))
        tail = tail.next
    return dummy.next

list1 = ListNode(5, ListNode(10, ListNode(20)))
list2 = ListNode(1, ListNode(30, ListNode(40)))
result = mergeKListsHeap([list1, list2])
assert result.val == 1
assert result.next.val == 5
assert result.next.next.val == 10
assert result.next.next.next.val == 20
assert result.next.next.next.next.val == 30
assert result.next.next.next.next.next.val == 40


def mergeKListsMergeSort(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # divide and conquer
    # divide list untill it will have 1 item
    # take pairs of lists and merge sort them
    # append result of each subsort to and array
    # assign the colection of sub array to lists variable

    if not lists:
        return None
    elif len(lists) == 1:
        return lists[0]
    elif len(lists) == 2:
        return mergeSort(lists[0], lists[1])
    else:
        pivot = len(lists) // 2
        list1 = mergeKLists(lists[0:pivot])
        list2 = mergeKLists(lists[pivot:len(lists)])
        return mergeSort(list1, list2)


def mergeSort(l1, l2):
    dummyNode = tail = ListNode(0, None)
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
    return dummyNode.next


list1 = ListNode(5, ListNode(10, ListNode(20)))
list2 = ListNode(1, ListNode(30, ListNode(40)))
list3 = ListNode(100, ListNode(300, ListNode(400, ListNode(500))))
list4 = None
list5 = None
result = mergeKListsMergeSort([list1, list2, list3, list4, list5])
assert result.val == 1
assert result.next.val == 5
assert result.next.next.val == 10
assert result.next.next.next.val == 20
assert result.next.next.next.next.val == 30
assert result.next.next.next.next.next.val == 40