"""
Author: Sai Sundeep Rayidi
Date: 6/11/2024

Description:
A Deque ADT implementation.
A deque (short for double-ended queue) data structure allows efficient (O(1)) insertion and deletion operations
on both the front and rear end.

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


class Node:
    def __init__(self, data, next_link, prev_link):
        self.data = data
        self.next = next_link
        self.prev = prev_link


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.deque_size = 0

    def is_empty(self):
        return self.head is None

    def size(self):
        return self.deque_size

    def push_left(self, data_item):
        new_node = Node(data_item, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.deque_size += 1
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        self.deque_size += 1

    def push_right(self, data_item):
        new_node = Node(data_item, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.deque_size += 1
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.deque_size += 1

    def pop_left(self):
        if self.head is None:
            return None

        if self.deque_size == 1:
            return_data = self.head.data
            self.head = None
            self.tail = None
        else:
            return_data = self.head.data
            next_head = self.head.next
            next_head.prev = None
            self.head = next_head
        self.deque_size -= 1
        return return_data

    def pop_right(self):
        if self.tail is None:
            return None

        if self.deque_size == 1:
            return_data = self.head.data
            self.head = None
            self.tail = None
        else:
            return_data = self.tail.data
            next_tail = self.tail.prev
            next_tail.next = None
            self.tail = next_tail
        self.deque_size -= 1
        return return_data

    def peek_right(self):
        if not self.tail:
            return
        return self.tail.data

    def peek_left(self):
        if not self.head:
            return
        return self.head.data

    def __str__(self):
        curr_node = self.head
        return_string = "Left::>> "
        while curr_node is not None:
            return_string += str(curr_node.data) + " "
            curr_node = curr_node.next
        return_string += "<<::Right"
        return return_string


def run_test_client():
    deque = Deque()
    deque.push_right(10)
    deque.push_right(20)
    deque.push_left(40)
    deque.push_left(30)
    print(deque)
    print(f"Peek Left {deque.peek_left()}")
    print(f"Peek Right {deque.peek_right()}")
    print(f"Deque Size: {deque.size()}")
    print(f"Is deque empty?: {deque.is_empty()}")
    deque.pop_left()
    deque.pop_right()
    print(deque)
    deque.pop_left()
    deque.pop_right()
    print(f"Deque Size: {deque.size()}")
    print(f"Is deque empty?: {deque.is_empty()}")


if __name__ == "__main__":
    run_test_client()







