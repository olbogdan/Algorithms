from collections import deque

def sort(nums):
    if len(nums) < 2:
        return nums
    else:
        mid = len(nums) // 2
        return merge(nums[:mid], nums[mid:])

def merge(left, right):
    if len(left) > 2:
        mid = len(left) // 2
        left = merge(left[:mid], left[mid:])
    else:
        if len(left) == 2 and left[0] > left[1]:
            left[0], left[1] = left[1], left[0]

    if len(right) > 2:
        mid = len(right) // 2
        right = merge(right[:mid], right[mid:])
    else:
        if len(right) == 2 and right[0] > right[1]:
            right[0], right[1] = right[1], right[0]

    result = []
    left = deque(left)
    right = deque(right)
    while left and right:
        if left[0] < right[0]:
            result.append(left.popleft())
        else:
            result.append(right.popleft())
    result.extend(left)
    result.extend(right)
    return result

array = [2, 1, -1, -2]
print(sort(array))

array = [5, 2, 3, 1]
print(sort(array))

array = [5,1,1,2,0,0]
print(sort(array))