def sort(array):
    for i in range(len(array)):
        for j in range(0, len(array)-i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

array = [-1, -2, 2, 1, 3, 4, 7, 5, 6, 6, 0, 10, 10, -18, -10]
print(sort(array))
assert sort(array) == [-18, -10, -2, -1, 0, 1, 2, 3, 4, 5, 6, 6, 7, 10, 10]

array = [10, -1, -2]
print(sort(array))
assert sort(array) == [-2, -1, 10]
