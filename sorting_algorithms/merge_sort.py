# Created by Sai at 6/6/2024

import numpy as np


def merge(arr, p, q, r):
    len_left_arr = len(arr[p:q+1])
    len_right_arr = len(arr[q+1:r+1])
    left_arr = [arr[p+i] for i in range(len_left_arr)]
    right_arr = [arr[j+q+1] for j in range(len_right_arr)]
    i = 0
    j = 0
    k = p
    while i < len_left_arr and j < len_right_arr:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len_left_arr:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len_right_arr:
        arr[k] = right_arr[j]
        j += 1
        k += 1


def merge_sort(arr, p, r):
    if p >= r:
        return
    q = ((p + r - 1) // 2)
    merge_sort(arr, p, q)
    merge_sort(arr, q+1, r)
    merge(arr, p, q, r)
    return arr


if __name__ == "__main__":
    sample_arr = np.random.randint(100, 999, 10)
    print(f"Original Array: {sample_arr}")
    sorted_arr = merge_sort(arr=sample_arr, p=0, r=len(sample_arr))
    print(f"Sorted Array: {sorted_arr}")
