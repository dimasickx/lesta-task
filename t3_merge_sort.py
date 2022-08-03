def merge_sort(array):
    if array is None:
        return
    if len(array) <= 1:
        return array
    left_arr = array[:len(array) // 2]
    right_arr = array[len(array) // 2:]
    a = merge_sort(left_arr)
    b = merge_sort(right_arr)
    arr1 = merge(a, b)
    return arr1


def merge(arr1, arr2):
    i = 0
    j = 0
    result_index = 0
    result_len = len(arr1) + len(arr2)
    result = [None for _ in range(result_len)]
    for _ in range(result_len):
        if i >= len(arr1):
            result[result_index] = arr2[j]
            j += 1
            result_index += 1
        elif j >= len(arr2):
            result[result_index] = arr1[i]
            i += 1
            result_index += 1
        elif arr1[i] <= arr2[j]:
            result[result_index] = arr1[i]
            i += 1
            result_index += 1
        else:
            result[result_index] = arr2[j]
            j += 1
            result_index += 1
    return result
