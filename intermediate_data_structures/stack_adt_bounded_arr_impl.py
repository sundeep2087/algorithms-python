# Created by Sai at 6/4/2024

import sys


class BoundedStack():
    def __init__(self, capacity):
        self._arr = []
        self._capacity = capacity

    def push(self, elem):
        if len(self._arr) < self._capacity:
            self._arr += [elem]
        else:
            print(f"Stack Overflow! Cannot insert beyond the preset limit of {self._capacity}.")

    def pop(self):
        if len(self._arr) == 0:
            print("Stack Underflow! Cannot pop from an empty stack.")
        else:
            return self._arr.pop()

    def __len(self):
        return len(self._arr)

    def __str__(self):
        return_string = ""
        for elem in self._arr:
            return_string = str(elem) + ' ' + return_string
        return return_string

    def is_empty(self):
        return len(self._arr) == 0

