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
    def __init__(self, key, left, right, parent):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def is_empty(self):
        return self.root is None

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
        self.size += 1

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
        if self.root is None:
            return
        while curr_node:
            if search_key == curr_node.key:
                return curr_node
            elif search_key < curr_node.key:
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
        if not curr_node:
            return None

        if curr_node.right:
            return self.minimum_node(curr_node.right)

        parent_node = curr_node.parent
        while parent_node and (parent_node.right == curr_node):
            curr_node = parent_node
            parent_node = parent_node.parent

        return parent_node

    def predecessor(self, curr_node):
        if not curr_node:
            return

        if curr_node.left:
            return self.maximum_node(curr_node.left)

        parent_node = curr_node.parent
        while parent_node and (curr_node == parent_node.left):
            curr_node = parent_node
            parent_node = parent_node.parent

        return parent_node

    def _transplant(self, node_u, node_v):
        if not self.root:
            return

        if not node_u.parent:
            self.root = node_v
        elif node_u == node_u.parent.left:
            node_u.parent.left = node_v
        else:
            node_u.parent.right = node_v

        if node_v:
            node_v.parent = node_u.parent

    def delete(self, curr_node):
        if not self.root:
            return

        if not curr_node.left:
            self._transplant(curr_node, curr_node.right)
        elif not curr_node.right:
            self._transplant(curr_node, curr_node.left)
        else:
            node_y = self.minimum_node(curr_node.right)
            if node_y != curr_node.right:
                self._transplant(node_y, node_y.right)
                node_y.right = curr_node.right
                node_y.right.parent = node_y
            self._transplant(curr_node, node_y)
            node_y.left = curr_node.left
            node_y.left.parent = node_y
        self.size -= 1

    def _height_recursive(self, node):
        if not node:
            return -1
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return max(left_height, right_height) + 1

    def height(self, node=None):
        if not node:
            return self._height_recursive(self.root)
        else:
            return self._height_recursive(node)

    def _recursive_depth(self, curr_node, search_node, depth=0):
        if not curr_node:
            return -1

        if curr_node == search_node:
            return depth

        left_depth = self._recursive_depth(curr_node.left, search_node, depth+1)
        if left_depth != -1:
            return left_depth

        right_depth = self._recursive_depth(curr_node.right, search_node, depth+1)
        if right_depth != -1:
            return right_depth

        return -1

    def depth(self, node):
        if not node:
            return -1
        return self._recursive_depth(self.root, node)


def run_test_client():
    bst = BinarySearchTree()
    bst.insert(3)
    bst.insert(11)
    bst.insert(7)
    bst.insert(1)
    bst.insert(24)
    bst.insert(6)
    bst.insert(42)
    print(f"Size of BST: {bst.size}")
    print(f"Tree Height: {bst.height()}")
    bst.inorder_traversal(bst.root)
    print(f"\nIs 99 Present? Location : {bst.search(bst.root, 99)}")
    print(f"\nIs 1 Present? Location : {bst.search(bst.root, 1)}")
    bst.insert(99)
    bst.insert(8)
    print(f"\nTree Height(11): {bst.height(bst.search(bst.root, 11))}")
    min_element_node = bst.minimum_node(bst.root)
    max_element_node = bst.maximum_node(bst.root)
    print(f"Minimum Element: {min_element_node.key}")
    print(f"Minimum Element: {max_element_node.key}")
    succ_8 = bst.successor(bst.search(bst.root, 8))
    print(f"Successor to 8: {succ_8.key}")
    bst.inorder_traversal(bst.root)
    print()
    print(f"Tree Height: {bst.height()}")
    succ_42 = bst.successor(bst.search(bst.root, 42))
    print(f"\nSuccessor to 42: {succ_42.key}")
    pred_8 = bst.predecessor(bst.search(bst.root, 8))
    print(f"Successor to 8: {pred_8.key}")
    bst.inorder_traversal(bst.root)
    print()
    print(f"Size of BST: {bst.size}")
    print(f"Tree Height: {bst.height()}")
    pred_42 = bst.predecessor(bst.search(bst.root, 42))
    print(f"\nSuccessor to 42: {pred_42.key}")
    pred_1 = bst.predecessor(bst.search(bst.root, 1))
    try:
        print(f"\nPredecessor of 1: {pred_1.key}")
    except AttributeError:
        print(f"No Predecessor 1!")
    succ_99 = bst.successor(bst.search(bst.root, 99))
    try:
        print(f"Successor to 99: {succ_99.key}")
    except AttributeError:
        print(f"No Successor to 99!")
    bst.delete(bst.search(bst.root, 99))
    bst.delete(bst.search(bst.root, 11))
    bst.delete(bst.search(bst.root, 1))
    print(f"Size of BST: {bst.size}")
    bst.inorder_traversal(bst.root)
    print(f"\nTree Height: {bst.height()}")
    print(f"\nTree Height(24): {bst.height(bst.search(bst.root, 24))}")


if __name__ == "__main__":
    run_test_client()
