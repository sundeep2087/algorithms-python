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
# import numpy as np
# np.random.seed(1000)

class AVLTreeNode:
    def __init__(self, key, unique_vizid):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.unique_vizid = unique_vizid


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

    def _rotate_left(self, node):
        y = node.right
        T2 = y.left

        y.left = node
        node.right = T2

        self.update_height(node)
        self.update_height(y)

        return y

    def _rotate_right(self, node):
        y = node.left
        T2 = y.right

        y.right = node
        node.left = T2

        self.update_height(node)
        self.update_height(y)

        return y

    def _insert_key(self, root, key):
        if not root:
            self._size += 1
            return AVLTreeNode(key, self._size)

        if key < root.key:
            root.left = self._insert_key(root.left, key)
        else:
            root.right = self._insert_key(root.right, key)

        self.update_height(root)
        balance = self.get_balance(root)

        # Left-Left Case
        if balance > 1 and key <= root.left.key:
            return self._rotate_right(root)

        # Right-Right Case
        if balance < -1 and key >= root.right.key:
            return self._rotate_left(root)

        # Right-Left Case
        if balance < -1 and key <= root.right.key:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        # Left-Right Case
        if balance > 1 and key >= root.left.key:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)

        return root

    def insert(self, key):
        self.root = self._insert_key(self.root, key)

    # Traversal Methods
    def _recursive_inorder_traversal(self, node, result):
        if not node:
            return
        self._recursive_inorder_traversal(node.left, result)
        result.append(node.key)
        self._recursive_inorder_traversal(node.right, result)

    def inorder_traversal(self, node=None):
        result = []
        if not node:
            self._recursive_inorder_traversal(self.root, result)
        self._recursive_inorder_traversal(node, result)
        return result

    def _recursive_preorder_traversal(self, node, result):
        if not node:
            return
        result.append(node.key)
        self._recursive_preorder_traversal(node.left, result)
        self._recursive_preorder_traversal(node.right, result)

    def preorder_traversal(self, node=None):
        result = []
        if not node:
            self._recursive_preorder_traversal(self.root, result)
        self._recursive_preorder_traversal(node, result)
        return result

    def _recursive_postorder_traversal(self, node, result):
        if not node:
            return
        self._recursive_postorder_traversal(node.left, result)
        self._recursive_postorder_traversal(node.right, result)
        result.append(node.key)

    def postorder_traversal(self, node=None):
        result = []
        if not node:
            self._recursive_postorder_traversal(self.root, result)
        self._recursive_postorder_traversal(node, result)
        return result

    # Tree Visualization Methods
    def _visualize(self, node, graph):
        if node is not None:
            graph.node(str(node.unique_vizid), label=str(node.key))
            if node.left:
                graph.edge(str(node.unique_vizid), str(node.left.unique_vizid))
                self._visualize(node.left, graph)
            if node.right:
                graph.edge(str(node.unique_vizid), str(node.right.unique_vizid))
                self._visualize(node.right, graph)

    def visualize(self):
        dg = Digraph()
        if self.root:
            dg.node(str(self.root.unique_vizid), label=str(self.root.key))
            self._visualize(self.root, dg)
        dg.render("./data/avl_tree2", format="png", cleanup=False)


def run_test_client():
    avl_tree = AVLTree()
    # a = (f"avl_tree.insert({i})" for i in np.random.randint(1, 50, 10))
    # for i in a:
    #     print(i)

    avl_tree.insert(2)
    avl_tree.insert(37)
    avl_tree.insert(33)
    avl_tree.insert(15)
    avl_tree.insert(32)
    avl_tree.insert(11)
    avl_tree.insert(15)
    avl_tree.insert(25)
    avl_tree.insert(17)
    avl_tree.insert(26)
    avl_tree.insert(40)
    avl_tree.insert(32)
    avl_tree.insert(2)
    avl_tree.insert(41)
    avl_tree.insert(3)

    inorder_traversal = avl_tree.inorder_traversal()
    print(f"Inorder Traversal: {inorder_traversal}")

    preorder_traversal = avl_tree.preorder_traversal()
    print(f"Preorder Traversal: {preorder_traversal}")

    postorder_traversal = avl_tree.postorder_traversal()
    print(f"Postorder Traversal: {postorder_traversal}")

    avl_tree.visualize()


if __name__ == "__main__":
    run_test_client()