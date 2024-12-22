"""
Author: Sai Sundeep Rayidi
Date: 12/20/2024

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


class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev, self.next = None, None


class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def dll_insert(self, curr_node):
        prev, next = self.right.prev, self.right
        curr_node.next, curr_node.prev = next, prev
        prev.next, next.prev = curr_node, curr_node

    def dll_remove(self, curr_node):
        prev, next = curr_node.prev, curr_node.next
        prev.next, next.prev = next, prev

    def get(self, key):
        if key in self.cache:
            self.dll_remove(self.cache[key])
            self.dll_insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.dll_remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.dll_insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.dll_remove(lru)
            del self.cache[lru.key]

    def print_lru(self):
        if len(self.cache) == 0:
            print(f"Empty Cache")
            return
        curr_node = self.left.next
        print("START ->", end=" ")
        while curr_node.next:
            print(f"({curr_node.key}:{curr_node.value})", end=" -> ")
            curr_node = curr_node.next
        print("END")


if __name__ == "__main__":
    lru = LRUCache(3)
    lru.put(1, 10)
    lru.put(2, 20)
    lru.put(3, 30)
    lru.put(4, 20)
    print(lru.get(1))
    print(lru.get(3))
    print(lru.get(2))
    lru.print_lru()
