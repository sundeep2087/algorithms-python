"""
Author: Sai Sundeep Rayidi
Date: 7/9/2024

Description:
Implements the Counting Sort Algorithm on an array of non-negative integer keys.

Additional Notes:
[Any additional notes or information you want to include.]

License: 
MIT License

Copyright (c) 2024 Sai Sundeep Rayidi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Contact:
[Optional: How to reach you for questions or collaboration.]

"""
import numpy as np
np.random.seed(3281)


def counting_sort(arr):
    result_arr = [0 for _ in range(len(arr))]
    max_elem_k = max(arr)
    auxiliary_arr = [0 for _ in range(max_elem_k+1)]
    for elem in arr:
        auxiliary_arr[elem] += 1
    for i in range(1, len(auxiliary_arr)):
        auxiliary_arr[i] = auxiliary_arr[i] + auxiliary_arr[i-1]
    for j in range(len(arr)-1, -1, -1):
        result_arr[auxiliary_arr[arr[j]]-1] = arr[j]
        auxiliary_arr[arr[j]] -= 1

    return result_arr


def counting_sort_handle_negatives(arr):
    result_arr = [0 for _ in range(len(arr))]
    min_elem = min(arr)
    if min_elem < 0:
        arr = [elem - min_elem for elem in arr]
    max_elem_k = max(arr)
    auxiliary_arr = [0 for _ in range(max_elem_k+1)]
    for elem in arr:
        auxiliary_arr[elem] += 1
    for i in range(1, len(auxiliary_arr)):
        auxiliary_arr[i] = auxiliary_arr[i] + auxiliary_arr[i-1]
    for j in range(len(arr)-1, -1, -1):
        result_arr[auxiliary_arr[arr[j]]-1] = arr[j]
        auxiliary_arr[arr[j]] -= 1
    result_arr = [elem + min_elem for elem in result_arr]
    return result_arr


def run_test_client():
    test_arrs = [
        list(np.random.randint(0, 3, 20)),
        list(np.random.randint(1, 20, 20)),
        list(np.random.randint(1, 100, 20)),
        list(np.random.randint(100, 999, 10)),
        list(np.random.randint(1, 1000, 10)),
        list(np.random.randint(1, 10000, 100))
    ]
    print(f"\n\n")
    for arr in test_arrs:
        print(f"Before Sorting: \n\t {arr}")
        result_arr = counting_sort(arr)
        print(f"After Sorting: \n\t {result_arr}")
        print("=" * 150)

    # Test Counting Sort with Negative Elements
    test_arrs = [
        list(np.random.randint(-10, 10, 10)),
        list(np.random.randint(-1, 1, 20)),
        list(np.random.randint(-20, 20, 20)),
        list(np.random.randint(-100, 0, 20)),
        list(np.random.randint(-999, 999, 10)),
        list(np.random.randint(-1000, 1000, 10)),
        list(np.random.randint(1, 10000, 100))
    ]
    for arr in test_arrs:
        print(f"Before Sorting: \n\t {arr}")
        result_arr = counting_sort_handle_negatives(arr)
        print(f"After Sorting: \n\t {result_arr}")
        print("=" * 150)


if __name__ == "__main__":
    run_test_client()
