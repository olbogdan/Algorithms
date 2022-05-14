def sort(array):
    if len(array) < 2:
        return array
    else:
        mid = len(array) // 2
        return merge_sort(array[:mid], array[mid:])

def merge_sort(left, right):
    left_array = []
    if len(left) > 2:
        mid = len(left) // 2
        left_array = merge_sort(left[:mid], left[mid:])
    else:
        if len(left) == 2 and left[0] > left[1]:
            left[0], left[1] = left[1], left[0]
        left_array = left
    right_array = []
    if len(right) > 2:
        mid = len(right) // 2
        right_array = merge_sort(right[:mid], right[mid:])
    else:
        if len(right) == 2 and right[0] > right[1]:
            right[0], right[1] = right[1], right[0]
        right_array = right
    if left_array and right_array and left_array[0] > right_array[0]:
        return right_array + left_array
    else:
        return left_array + right_array

array = [2, 1, -1, -2]
print(sort(array))