# Created by Sai at 6/27/2024
import numpy as np
np.random.seed(2378)


# Selection Sort - For each position, find the smallest element and place it in current index. Continue until n-1

def selection_sort(arr):
    for i in range(len(arr)-1):
        curr_key = arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] < curr_key:
                arr[i] = arr[j]
                arr[j] = curr_key
                curr_key = arr[i]


def run_test_client():
    test_arrs = [
        list(np.random.randint(1, 100, 10)),
        list(np.random.randint(1, 1000, 10)),
        list(np.random.randint(1, 10000, 100)),
        list(np.random.randint(-10000, 10000, 100)),
    ]
    for arr in test_arrs:
        print(f"Before Sorting: \n\t {arr}")
        selection_sort(arr)
        print(f"After Sorting: \n\t {arr}")
        print("=" * 150)


if __name__ == "__main__":
    run_test_client()