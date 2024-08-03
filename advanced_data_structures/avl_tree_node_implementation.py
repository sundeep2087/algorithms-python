"""
Author: Sai Sundeep Rayidi
Date: 8/3/2024

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

from graphviz import Digraph


class AVLTreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.height = 1
        self.count = 1


class AVLTree:
    def __init__(self):
        self.root = None
        self._size = 0

    def is_empty(self):
        return self.root is None

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def update_height(self, node):
        if node:
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def rotate_left(self, node):
        y = node.right
        T2 = y.left

        y.left = node
        node.right = T2

        self.update_height(node)
        self.update_height(y)

        return y

    def rotate_right(self, node):
        y = node.left
        T2 = y.right

        y.right = node
        node.left = T2

        self.update_height(node)
        self.update_height(y)

        return y

    def _insert_key(self, root, key):
        if not root:
            return AVLTreeNode(key)

        if key < root.key:
            root.left = self._insert_key(root.left, key)
        elif key > root.key:
            root.right = self._insert_key(root.right, key)
        else:
            root.count += 1
            return root

        self.update_height(root)
        balance = self.get_balance(root)

        # Left-Left Case
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        # Right-Right Case
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        # Right-Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        # Left-Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        return root

    def insert(self, key):
        self.root = self._insert_key(self.root, key)

    # Traversal Methods
    def _recursive_inorder_traversal(self, node, result):
        if not node:
            return
        self._recursive_inorder_traversal(node.left, result)
        result.extend([node.key] * node.count)
        self._recursive_inorder_traversal(node.right, result)

    def inorder_traversal(self, node=None):
        if not self.root:
            return
        result = []
        if not node:
            self._recursive_inorder_traversal(self.root, result)
        self._recursive_inorder_traversal(node, result)
        return result

    # Tree Visualization Methods
    def _visualize(self, node, graph):
        if node is not None:
            if node.left:
                graph.node(str(node.key))
                graph.edge(str(node.key), str(node.left.key))
                self._visualize(node.left, graph)
            if node.right:
                graph.node(str(node.key))
                graph.edge(str(node.key), str(node.right.key))
                self._visualize(node.right, graph)

    def visualize(self):
        dg = Digraph()
        if self.root:
            dg.node(str(self.root.key))
            self._visualize(self.root, dg)
        dg.render("./data/avl_tree", format="png", cleanup=False)


def run_test_client():
    avl_tree = AVLTree()
    avl_tree.insert(40)
    avl_tree.insert(27)
    avl_tree.insert(1)
    avl_tree.insert(35)
    avl_tree.insert(41)
    avl_tree.insert(8)
    avl_tree.insert(32)
    avl_tree.insert(36)
    avl_tree.insert(13)
    avl_tree.insert(44)
    avl_tree.insert(8)
    avl_tree.insert(8)
    avl_tree.insert(8)

    inorder_traversal = avl_tree.inorder_traversal()
    print(inorder_traversal)
    avl_tree.visualize()


if __name__ == "__main__":
    run_test_client()