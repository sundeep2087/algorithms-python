# Created by Sai at 7/3/2024

class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None
        self._size = 0

    # Basic Operations

    def is_empty(self):
        return self.root is None

    def __len__(self):
        return self._size

    def insert(self, root_node, key):
        new_node = Node(key, None, None)
        if self.root is None:
            self.root = new_node
            self._size += 1
            return

        curr_node = root_node
        if key <= curr_node.key:
            if curr_node.left is None:
                curr_node.left = new_node
                self._size += 1
            else:
                self.insert(curr_node.left, key)
        else:
            if curr_node.right is None:
                curr_node.right = new_node
                self._size += 1
            else:
                self.insert(curr_node.right, key)

    def find_node(self, search_key):
        return self._recursive_find_node(self.root, search_key)

    def _recursive_find_node(self, curr_node, search_key):
        if curr_node is None or curr_node.key == search_key:
            return curr_node

        if search_key < curr_node.key:
            return self._recursive_find_node(curr_node.left, search_key)
        else:
            return self._recursive_find_node(curr_node.right, search_key)

    def find_all(self, search_key):
        nodes_list = []
        self._find_all_nodes_recursive(self.root, search_key, nodes_list)
        return nodes_list

    def _find_all_nodes_recursive(self, curr_node, search_key, nodes_list):
        if not curr_node:
            return

        self._find_all_nodes_recursive(curr_node.left, search_key, nodes_list)
        if curr_node.key == search_key:
            nodes_list.append(curr_node)
        self._find_all_nodes_recursive(curr_node.right, search_key, nodes_list)

    # Traversal Methods
    def preorder_traversal(self, curr_node):
        if not curr_node:
            return
        print(f"{curr_node.key}", end=" ")
        self.preorder_traversal(curr_node.left)
        self.preorder_traversal(curr_node.right)

    def inorder_traversal(self, curr_node):
        if not curr_node:
            return
        self.inorder_traversal(curr_node.left)
        print(f"{curr_node.key}", end=" ")
        self.inorder_traversal(curr_node.right)

    def postorder_traversal(self, curr_node):
        if not curr_node:
            return
        self.postorder_traversal(curr_node.left)
        self.postorder_traversal(curr_node.right)
        print(f"{curr_node.key}", end=" ")

    # Additional Useful Methods

    def is_leaf(self, node):
        return node.left is None and node.right is None

    def get_height(self):
        return self._get_height_recursive(self.root)

    def _get_height_recursive(self, root):
        if not root:
            return 0

        left_height = self._get_height_recursive(root.left)
        right_height = self._get_height_recursive(root.right)
        return max(left_height, right_height) + 1


def run_test_client():
    bin_tree = BinaryTree()
    data_elements = [12, 5, 23, 9, 17, 10, 1, 3, 26, 10, 12, 10]
    for i in data_elements:
        bin_tree.insert(bin_tree.root, i)

    print(f"In-Order Traversal -")
    bin_tree.inorder_traversal(bin_tree.root)
    print(f"\nPre-Order Traversal -")
    bin_tree.preorder_traversal(bin_tree.root)
    print(f"\nPost-Order Traversal -")
    bin_tree.postorder_traversal(bin_tree.root)

    print(f"\nNumber of Nodes: {len(bin_tree)}")

    print(f"Key 17 is present at Node: {bin_tree.find_node(17)}")

    print(f"List of Nodes with key 10:\n\t {bin_tree.find_all(10)}")

    print(f"Height of the Tree: {bin_tree.get_height()}")


if __name__ == "__main__":
    run_test_client()
