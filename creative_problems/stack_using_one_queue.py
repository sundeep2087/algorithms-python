"""
Author: Sai Sundeep Rayidi
Date: 7/7/2024

Description:
A stack implementation, that makes use of single queue ADT with its enqueue and dequeue operations.

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

from intermediate_data_structures.queue_adt_node_implementation import LLQueue


class Stack:
    def __init__(self):
        self._queue = LLQueue()

    def push(self, data):
        self._queue.enqueue(data)
        queue_len = self._queue.size()
        for _ in range(queue_len-1):
            self._queue.enqueue(self._queue.dequeue())

    def pop(self):
        return self._queue.dequeue()

    def is_empty(self):
        return self._queue.size() == 0

    def __len__(self):
        return self._queue.size()

    def peek(self):
        return self._queue.get_front()


def run_test_client():
    stack = Stack()
    stack.push(10)
    stack.push(298)
    stack.push("Halo")
    stack.push(234)
    stack.push(89)
    stack.push("Hi")
    stack.push("Hello")
    print(f"Length of Stack: {len(stack)}")
    stack.pop()
    stack.pop()
    print(f"Top Element: {stack.peek()}")
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    print(f"Top Element: {stack.peek()}")
    print(f"Length of Stack: {len(stack)}")

    stack.push("Green")
    stack.push("Red")
    print(f"Popped: {stack.pop()}")
    stack.push("Pegion")
    print(f"Popped: {stack.pop()}")
    print(f"Top Element: {stack.peek()}")
    print(f"Length of Stack: {len(stack)}")


if __name__ == "__main__":
    run_test_client()
