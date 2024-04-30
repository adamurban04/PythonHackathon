def max_heapify(arr, len_arr, parent_idx):
    largest = parent_idx
    left_child = 2 * parent_idx + 1
    right_child = 2 * parent_idx + 2

    if left_child < len_arr and arr[left_child] > arr[largest]:
        largest = left_child
    if right_child < len_arr and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != parent_idx:
        arr[largest], arr[parent_idx] = arr[parent_idx], arr[largest]
        max_heapify(arr, len_arr, largest)
    
def heap_sort(arr):
    len_arr = len(arr)
    for i in range(len_arr//2, -1, -1):
        max_heapify(arr, len_arr, i)
    for i in range(len_arr - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, i, 0)