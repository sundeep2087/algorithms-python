# Created by Sai at 6/26/2024

import numpy as np
np.random.seed(2378)


# Insertion Sort - For each element located at index 1 through n, find its position relative to the sorted left portion of the array.

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


def run_test_client():
    test_arrs = [
        list(np.random.randint(1, 100, 10)),
        list(np.random.randint(1, 1000, 10)),
        list(np.random.randint(1, 10000, 100)),
        list(np.random.randint(-10000, 10000, 100)),
    ]
    for arr in test_arrs:
        print(f"Before Sorting: \n\t {arr}")
        insertion_sort(arr)
        print(f"After Sorting: \n\t {arr}")
        print("=" * 150)


if __name__ == "__main__":
    run_test_client()