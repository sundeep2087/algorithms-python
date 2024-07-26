"""
Author: Sai Sundeep Rayidi
Date: 7/24/2024

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

from intermediate_data_structures.queue_adt_node_implementation import LLQueue


class Node:
    def __init__(self, key, color="red"):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = color


class RedBlackTree:
    def __init__(self):
        self._NIL = Node(None, "black")
        self.root = self._NIL
        self._size = 0

    def is_empty(self):
        return self.root is None

    def left_rotate(self, node_x):
        if node_x.right == self._NIL:
            raise ValueError("Cannot Perform Left Rotation since right child of node is NIL")
        node_y = node_x.right
        node_x.right = node_y.left

        if node_y.left != self._NIL:
            node_y.left.parent = node_x

        node_y.parent = node_x.parent
        if node_x.parent == self._NIL:
            self.root = node_y
        elif node_x == node_x.parent.left:
            node_x.parent.left = node_y
        else:
            node_x.parent.right = node_y

        node_y.left = node_x
        node_x.parent = node_y

    def right_rotate(self, node_x):
        if node_x.left == self._NIL:
            raise ValueError(f"Cannot perform right rotation since left child of node is NIL")
        node_y = node_x.left
        node_x.left = node_y.right

        if node_y.right != self._NIL:
            node_y.right.parent = node_x

        node_y.parent = node_x.parent
        if node_x.parent == self._NIL:
            self.root = node_y
        elif node_x.parent.right == node_x:
            node_x.parent.right = node_y
        else:
            node_x.parent.left = node_y

        node_y.right = node_x
        node_x.parent = node_y

    def insert_fixup(self, node_z):
        while node_z != self.root and node_z.parent.color == "red":
            if node_z.parent == node_z.parent.parent.left:

                node_y = node_z.parent.parent.right

                if node_y.color == "red":
                    node_z.parent.color = "black"
                    node_y.color = "black"
                    node_z.parent.parent.color = "red"
                    node_z = node_z.parent.parent
                else:
                    if node_z == node_z.parent.right:
                        node_z = node_z.parent
                        self.left_rotate(node_z)
                    node_z.parent.color = "black"
                    node_z.parent.parent.color = "red"
                    self.right_rotate(node_z.parent.parent)
            else:
                node_y = node_z.parent.parent.left

                if node_y.color == "red":
                    node_z.parent.parent.color = "red"
                    node_z.parent.color = "black"
                    node_y.color = "black"
                    node_z = node_z.parent.parent
                else:
                    if node_z == node_z.parent.left:
                        node_z = node_z.parent
                        self.right_rotate(node_z)
                    node_z.parent.color = "black"
                    node_z.parent.parent.color = "red"
                    self.left_rotate(node_z.parent.parent)

        self.root.color = "black"

    def insert(self, insert_key):
        new_node = Node(insert_key, color="red")
        new_node.left = self._NIL
        new_node.right = self._NIL

        curr_node = self.root
        parent = self._NIL

        while curr_node != self._NIL:
            parent = curr_node
            if new_node.key < curr_node.key:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

        new_node.parent = parent

        if parent == self._NIL:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        self.insert_fixup(new_node)

    def inorder_traversal(self, curr_node):
        if not curr_node:
            return
        self.inorder_traversal(curr_node.left)
        if curr_node.key is not None:
            print(curr_node.key, end=" ")
        self.inorder_traversal(curr_node.right)

    def preorder_traversal(self, curr_node):
        if not curr_node:
            return
        if curr_node.key is not None:
            print(curr_node.key, end=" ")
        self.preorder_traversal(curr_node.left)
        self.preorder_traversal(curr_node.right)

    def postorder_traversal(self, curr_node):
        if not curr_node:
            return
        self.postorder_traversal(curr_node.left)
        self.postorder_traversal(curr_node.right)
        if curr_node.key is not None:
            print(curr_node.key, end=" ")

    def levelorder_traversal(self, curr_node):
        if not curr_node:
            return []

        queue = LLQueue()
        queue.enqueue(curr_node)

        while queue:
            curr_level_nodes_count = len(queue)

            for i in range(curr_level_nodes_count):
                next_node = queue.dequeue()
                if next_node != self._NIL:
                    print(next_node.key, end=" ")

                if next_node.left:
                    queue.enqueue(next_node.left)
                if next_node.right:
                    queue.enqueue(next_node.right)
            print()

    def search(self, search_key):
        curr_node = self.root
        while curr_node != self._NIL and curr_node.key != search_key:
            if search_key < curr_node.key:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        return curr_node if curr_node != self._NIL else None

    def minimum_node(self, curr_node):
        if not self.root:
            return
        while curr_node.left != self._NIL:
            curr_node = curr_node.left
        return curr_node

    def maximum_node(self, curr_node):
        while curr_node.right != self._NIL:
            curr_node = curr_node.right
        return curr_node

    def transplant(self, node_u, node_v):
        if node_u.parent == self._NIL:
            self.root = node_v
        elif node_u == node_u.parent.right:
            node_u.parent.right = node_v
        else:
            node_u.parent.left = node_v
        if node_v:
            node_v.parent = node_u.parent

    def _delete_fixup(self, x_node):
        while x_node != self.root and x_node.color == "black":
            if x_node == x_node.parent.left:
                w_node = x_node.parent.right
                if w_node.color == "red":
                    w_node.color = "black"
                    x_node.parent.color = "red"
                    self.left_rotate(x_node.parent)
                    w_node = x_node.parent.right
                if w_node.left.color == "black" and w_node.right.color == "black":
                    w_node.color = "red"
                    x_node = x_node.parent
                else:
                    if w_node.right.color == "black":
                        w_node.left.color = "black"
                        w_node.color = "red"
                        self.right_rotate(w_node)
                        w_node = x_node.parent.right
                    w_node.color = x_node.parent.color
                    x_node.parent.color = "black"
                    w_node.right.color = "black"
                    self.left_rotate(x_node.parent)
                    x_node = self.root
            else:
                w_node = x_node.parent.left
                if w_node.color == "red":
                    w_node.color = "black"
                    w_node.parent.color = "red"
                    self.right_rotate(x_node.parent)
                    w_node = x_node.parent.left
                if w_node.right.color == "black" and w_node.left.color == "black":
                    w_node.color = "red"
                    x_node = x_node.parent
                else:
                    if w_node.left.color == "black":
                        w_node.right.color = "black"
                        w_node.color = "red"
                        self.left_rotate(w_node)
                        w_node = x_node.parent.left
                    w_node.color = x_node.parent.color
                    x_node.parent.color = "black"
                    w_node.left.color = "black"
                    self.right_rotate(x_node.parent)
                    x_node = self.root
        x_node.color = "black"

    def delete(self, delete_key):
        node = self.search(delete_key)
        if node is self._NIL:
            print(f"No node in tree with key {delete_key}")
            return

        original_color = node.color
        if node.left == self._NIL:
            child = node.right
            self.transplant(node, node.right)
        elif node.right == self._NIL:
            child = node.left
            self.transplant(node, node.left)
        else:
            successor = self.minimum_node(node.right)
            original_color = successor.color
            child = successor.right

            if successor.parent == node:
                child.parent = successor
            else:
                self.transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor
            self.transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor
            successor.color = node.color

        if original_color == "black":
            self._delete_fixup(child)


def run_test_client():
    rb_tree = RedBlackTree()
    rb_tree.insert(2)
    rb_tree.insert(3)
    rb_tree.insert(4)
    rb_tree.insert(7)
    rb_tree.insert(11)
    rb_tree.insert(9)
    rb_tree.insert(6)
    rb_tree.insert(14)
    rb_tree.insert(18)
    rb_tree.insert(20)
    rb_tree.insert(23)
    rb_tree.insert(8)
    print(f"Inorder Traversal - ")
    rb_tree.inorder_traversal(rb_tree.root)
    print(f"\nPreorder Traversal - ")
    rb_tree.preorder_traversal(rb_tree.root)
    print(f"\npostorder Traversal - ")
    rb_tree.postorder_traversal(rb_tree.root)
    print(f"\nlevelorder Traversal - ")
    rb_tree.levelorder_traversal(rb_tree.root)
    print(f"Node with key 11 is found at - {rb_tree.search(11)}")
    print(f"Node with key 100 is found at - {rb_tree.search(100)}")
    rb_tree.delete(2)
    rb_tree.delete(3)
    rb_tree.delete(4)
    rb_tree.delete(7)
    rb_tree.delete(11)
    rb_tree.delete(9)
    rb_tree.delete(6)
    rb_tree.delete(14)
    rb_tree.delete(18)
    rb_tree.inorder_traversal(rb_tree.root)
    rb_tree.delete(20)
    rb_tree.delete(23)
    rb_tree.delete(8)
    rb_tree.inorder_traversal(rb_tree.root)


if __name__ == "__main__":
    run_test_client()
