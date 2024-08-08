"""
Author: Sai Sundeep Rayidi
Date: 8/8/2024

Description:
[Description of what the file does, its purpose, etc.]

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

import random
import numpy as np


class QuickSort:
    def __init__(self, data, randomized=False):
        if isinstance(data, list) is False:
            raise ValueError("Data must be of type list!!!")
        self.data = data
        self.randomized = randomized

    def sort(self):
        if not self.data:
            return
        self._quick_sort(0, len(self.data) - 1)

    def _quick_sort(self, low, high):
        if low < high:
            pivot_index = self._partition(low, high)
            self._quick_sort(low, pivot_index - 1)
            self._quick_sort(pivot_index+1, high)

    def _partition(self, low, high):
        if self.randomized:
            random_pivot_index = random.randint(low, high)
            self.data[random_pivot_index], self.data[high] = self.data[high], self.data[random_pivot_index]

        pivot = self.data[high]
        i = low - 1
        for j in range(low, high):
            if self.data[j] < pivot:
                i += 1
                self.data[i], self.data[j] = self.data[j], self.data[i]

        self.data[i+1], self.data[high] = self.data[high], self.data[i+1]
        return i + 1


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
        sorter = QuickSort(arr, True)
        sorter.sort()
        # print(f"After Sorting: \n\t {arr}")
        print(f"After Sorting: \n\t {sorter.data}")
        print("=" * 150)


if __name__ == "__main__":
    run_test_client()