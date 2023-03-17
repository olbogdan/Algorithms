from collections import deque

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        l = arr[:mid]
        r = arr[mid:]
        merge_sort(l)
        merge_sort(r)

        l_index = 0
        r_index = 0
        main_arr_index = 0
        while l_index < len(l) and r_index < len(r):
            if l[l_index] > r[r_index]:
                arr[main_arr_index] = r[r_index]
                r_index += 1
            else:
                arr[main_arr_index] = l[l_index]
                l_index += 1
            main_arr_index += 1

        while l_index < len(l):
            arr[main_arr_index] = l[l_index]
            l_index += 1
            main_arr_index += 1
        while r_index < len(r):
            arr[main_arr_index] = r[r_index]
            r_index += 1
            main_arr_index += 1
    return arr

# Second solution:

def sort(arr):
    if len(arr) < 2:
        return arr
    else:
        mid = len(arr) // 2
        return merge(arr[:mid], arr[mid:])

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
assert merge_sort(array) == [-2, -1, 1, 2]
print(merge_sort(array))

array = [5, 2, 3, 1]
assert merge_sort(array) == [1, 2, 3, 5]
print(merge_sort(array))

array = [5,1,1,2,0,0]
assert merge_sort(array) == [0, 0, 1, 1, 2, 5]
print(merge_sort(array))

array = [2, 1, -1, -2]
assert sort(array) == [-2, -1, 1, 2]
print(sort(array))

array = [5, 2, 3, 1]
assert sort(array) == [1, 2, 3, 5]
print(sort(array))

array = [5,1,1,2,0,0]
assert sort(array) == [0, 0, 1, 1, 2, 5]
print(sort(array))