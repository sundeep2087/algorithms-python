# Created by Sai at 6/27/2024

import numpy as np
np.random.seed(1621)


def bubble_sort(arr):
    for i in range(len(arr)-1):
        no_swaps = True
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                no_swaps = False
        # print(arr)        # Debug
        if no_swaps:
            break


def run_test_client():
    test_arrs = [
        list(np.random.randint(-1, 2, 20)),
        list(np.random.randint(1, 100, 10)),
        list(np.random.randint(1, 1000, 10)),
        list(np.random.randint(1, 10000, 100)),
        list(np.random.randint(-10000, 10000, 100)),
    ]
    for arr in test_arrs:
        print(f"Before Sorting: \n\t {arr}")
        bubble_sort(arr)
        print(f"After Sorting: \n\t {arr}")
        print("=" * 150)


if __name__ == "__main__":
    run_test_client()
