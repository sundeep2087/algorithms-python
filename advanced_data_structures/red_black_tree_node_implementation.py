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


    def insert(self, key):
        node_z = Node(key=key, left=None, right=None, parent=None, color=None)
        node_z.left = self.nil
        node_z.right = self.nil
        node_z.color = "red"

        node_x = self.root
        node_y = self.nil
        while node_x is not self.nil:
            node_y = node_x
            if node_z.key < node_x.key:
                node_x = node_x.left
            else:
                node_x = node_x.right

        node_z.parent = node_y
        if node_y is self.nil:
            self.root = node_z
        elif node_z.key < node_y.key:
            node_y.left = node_z
        else:
            node_y.right = node_z

        self.insert_fixup(node_z)

