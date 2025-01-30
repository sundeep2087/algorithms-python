"""
Author: Sai Sundeep Rayidi
Date: 1/29/2025

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
from typing import Optional
from intermediate_data_structures.binary_tree_node_implementation import BinaryTree, Node
from collections import deque


def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
    def find_target_node(node, k):
        if not node:
            return None

        if node.val == k:
            return node

        left_res = find_target_node(node.left, k)
        if left_res:
            return left_res
        return find_target_node(node.right, k)

    parent_map = {}

    def build_parent_map(node):
        if node.left:
            parent_map[node.left] = node
            build_parent_map(node.left)
        if node.right:
            parent_map[node.right] = node
            build_parent_map(node.right)

    def bfs(start_node):
        queue = deque([start_node])
        visited = set()
        visited.add(start_node)

        while queue:
            node = queue.popleft()

            if not node.left and not node.right:
                return node

            if node.left and node.left not in visited:
                visited.add(node.left)
                queue.append(node.left)
            if node.right and node.right not in visited:
                visited.add(node.right)
                queue.append(node.right)
            if node != root and parent_map[node] not in visited:
                visited.add(parent_map[node])
                queue.append(parent_map[node])

    target_node = find_target_node(root, k)
    closest_leaf_node = bfs(target_node)
    return closest_leaf_node.val


if __name__ == "__main__":
    bin_tree = BinaryTree()
    root = [1,2,3,4, None, None, None,5, None,6]
    for i in root:
        bin_tree.insert(bin_tree.root, i)
    print(find_closest_leaf(bin_tree.root, 4))

    bin_tree = BinaryTree()
    root = [1, 3, 2]
    for i in root:
        bin_tree.insert(bin_tree.root, i)
    print(find_closest_leaf(bin_tree.root, 2))

