"""
Author: Sai Sundeep Rayidi
Date: 7/18/2024

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
    def __init__(self, key, left_node, right_node, parent_node):
        self.key = key
        self.left = left_node
        self.right = right_node
        self.parent = parent_node


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, insert_key):
        new_node = Node(insert_key, None, None, None)
        curr_node = self.root
        parent_node = None
        while curr_node:
            parent_node = curr_node
            if new_node.key < curr_node.key:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        new_node.parent = parent_node
        if not parent_node:
            self.root = new_node
        elif new_node.key < parent_node.key:
            parent_node.left = new_node
        else:
            parent_node.right = new_node

    # Traversal Methods
    def inorder_traversal(self, curr_node):
        if not curr_node:
            return
        self.inorder_traversal(curr_node.left)
        print(curr_node.key, end=" ")
        self.inorder_traversal(curr_node.right)

    def preorder_traversal(self, curr_node):
        if not curr_node:
            return
        print(curr_node.key, end=" ")
        self.preorder_traversal(curr_node.left)
        self.preorder_traversal(curr_node.right)

    def postorder_traversal(self, curr_node):
        if not curr_node:
            return
        self.postorder_traversal(curr_node.left)
        self.postorder_traversal(curr_node.right)
        print(curr_node.key, end=" ")

    def search(self, curr_node, search_key):
        if not self.root:
            return
        while curr_node and search_key != curr_node.key:
            if search_key < curr_node.key:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        return curr_node

    def minimum_node(self, curr_node):
        if not self.root:
            return
        while curr_node.left:
            curr_node = curr_node.left
        return curr_node

    def maximum_node(self, curr_node):
        if not self.root:
            return
        while curr_node.right:
            curr_node = curr_node.right
        return curr_node

    def successor(self, curr_node):
        if not self.root:
            return
        if curr_node.right:
            self.minimum_node(curr_node.right)
        else:
            parent_node = curr_node.parent
            while parent_node and curr_node == parent_node.right:
                curr_node = parent_node
                parent_node = parent_node.parent
            return parent_node


def run_test_client():
    bst = BinarySearchTree()
    bst.insert(3)
    bst.insert(11)
    bst.insert(7)
    bst.insert(1)
    bst.insert(24)
    bst.insert(6)
    bst.insert(42)
    bst.inorder_traversal(bst.root)
    print(f"\nIs 99 Present? Location : {bst.search(bst.root, 99)}")
    print(f"\nIs 1 Present? Location : {bst.search(bst.root, 1)}")
    bst.insert(99)
    bst.insert(8)
    min_element_node = bst.minimum_node(bst.root)
    max_element_node = bst.maximum_node(bst.root)
    print(f"Minimum Element: {min_element_node.key}")
    print(f"Minimum Element: {max_element_node.key}")
    succ_8 = bst.successor(bst.search(bst.root, 8))
    print(f"Successor to 8: {succ_8.key}")
    succ_42 = bst.successor(bst.search(bst.root, 42))
    print(f"Successor to 42: {succ_42.key}")


if __name__ == "__main__":
    run_test_client()
