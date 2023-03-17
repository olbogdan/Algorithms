def sort(array):
    for i in range(len(array)):
        index_of_current_min = i
        for j in range(i+1, len(array)):
            if array[j] < array[index_of_current_min]:
                index_of_current_min = j
        if index_of_current_min != i:
            array[index_of_current_min], array[i] = array[i], array[index_of_current_min]
    return array


def sort2(array):
    for i in range(0, len(array) - 1):
        if array[i] > array[i+1]:
            array[i+1], array[i] = array[i], array[i+1]

            prev_item_index = i-1
            current_item_index = i
            while prev_item_index >= 0 and array[prev_item_index] > array[current_item_index]:
                array[prev_item_index], array[current_item_index] = array[current_item_index], array[prev_item_index]
                prev_item_index -= 1
                current_item_index -= 1
    return array


array = [2, 1, 3, 4, 7, 5, 6, 6, 0, 10, 10]
print(sort(array))
assert sort(array) == [0, 1, 2, 3, 4, 5, 6, 6, 7, 10, 10]
assert sort(array) == sort2(array)
