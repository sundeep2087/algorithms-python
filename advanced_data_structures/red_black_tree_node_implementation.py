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


class Node:
    def __init__(self, key, left, right, parent, color):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color


class RedBlackTree:
    def __init__(self):
        self.root = None
        self.nil = Node(None,None, None, None, "black")
        self._size = 0

    def is_empty(self):
        return self.root is None

    def left_rotate(self, node_x):
        node_y = node_x.right
        node_x.right = node_y.left
        if node_y.left is not None:
            node_y.left.parent = node_x

        node_y.parent = node_x.parent
        if node_x.parent is None:
            self.root = node_y
        elif node_x == node_x.parent.left:
            node_x.parent.left = node_y
        else:
            node_x.parent.right = node_y

        node_y.left = node_x
        node_x.parent = node_y

    def right_rotate(self, node_x):
        node_y = node_x.left
        node_x.left = node_y.right
        if node_y.right is not None:
            node_y.right.parent = node_x

        node_y.parent = node_x.parent
        if node_x.parent is None:
            self.root = node_y
        elif node_x.parent.right == node_x:
            node_x.parent.right = node_y
        else:
            node_x.parent.left = node_y

        node_y.right = node_x
        node_x.parent = node_y

    def insert_fixup(self, node_z):
        while node_z.parent.color == "red":
            if node_z.parent is node_z.parent.parent.left:

                node_y = node_z.parent.parent.right

                if node_y.color == "red":
                    node_z.parent.color = "black"
                    node_y.color = "black"
                    node_z.parent.parent.color = "red"
                    node_z = node_z.parent.parent
                else:
                    if node_z is node_z.parent.right:
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
                    if node_z is node_z.parent.left:
                        node_z = node_z.parent
                        self.right_rotate(node_z)
                    node_z.parent.color = "black"
                    node_z.parent.parent.color = "red"
                    self.left_rotate(node_z.parent.parent)

        self.root.color = "black"

    def insert(self, insert_key):
        new_node = Node(key=insert_key, left=None, right=None, parent=None, color=None)
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.color = "red"

        curr_node = self.root
        parent = self.nil
        while curr_node:
            parent = curr_node
            if new_node.key < curr_node.key:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

        new_node.parent = parent
        if parent is self.nil:
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
        print(curr_node.key, end=" ")
        self.inorder_traversal(curr_node.right)


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
    rb_tree.inorder_traversal(rb_tree.root)


if __name__ == "__main__":
    run_test_client()
