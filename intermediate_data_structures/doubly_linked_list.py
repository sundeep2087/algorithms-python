# Created by Sai at 7/2/2024

class Node:
    def __init__(self, data, next_node, prev_node):
        self.data = data
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self):
        return self.head is None

    def get_node(self, data_element):
        curr_node = self.head
        while curr_node and curr_node.data != data_element:
            curr_node = curr_node.next
        if curr_node is not None:
            return curr_node
        else:
            return None

    def insert_after(self, new_node, before_node):
        new_node.prev = before_node
        if before_node.next is None:
            self.tail = new_node
        else:
            before_node.next.prev = new_node
            new_node.next = before_node.next
        before_node.next = new_node
        self._size += 1

    def insert_before(self, new_node, after_node):
        new_node.next = after_node
        if after_node.prev is None:
            self.head = new_node
        else:
            new_node.prev = after_node.prev
            after_node.prev.next = new_node
        after_node.prev = new_node
        self._size += 1

    def insert_at_beginning(self, data_element):
        new_node = Node(data_element, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self._size += 1
            return
        self.insert_before(new_node, self.head)

    def insert_at_end(self, data_element):
        new_node = Node(data_element, None, None)
        if self.tail is None:
            self.insert_before(new_node, self.head)
        else:
            self.insert_after(new_node, self.tail)

    def remove_node(self, node):
        if node.prev is None:
            self.head = node.next
            self.head.prev = None
        elif node.next is None:
            self.tail = node.prev
            self.tail.next = None
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
        self._size -= 1

    def remove_from_beginning(self):
        if not self.head:
            return "Empty List! Not items to remove."
        removed_node = self.head
        self.head = self.head.next
        self.head.prev = None
        return removed_node

    def remove_from_end(self):
        if not self.tail:
            return "Empty List! No items to remove."
        removed_node = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        return removed_node

    def __str__(self):
        return_str = ""
        curr_node = self.head
        while curr_node:
            return_str += str(curr_node.data) + " "
            curr_node = curr_node.next
        return return_str

    def __len__(self):
        return self._size

    class DLLIterator:
        def __init__(self, curr_node):
            self.curr_node = curr_node

        def __iter__(self):
            return self

        def __next__(self):
            if self.curr_node:
                node = self.curr_node
                self.curr_node = self.curr_node.next
                return node
            else:
                raise StopIteration

    def __iter__(self):
        return self.DLLIterator(self.head)


def run_test_client():
    dll = DoublyLinkedList()
    dll.insert_at_beginning(100)
    dll.insert_at_end(200)
    dll.insert_at_beginning(50)
    dll.insert_at_end(250)
    dll.insert_at_end(350)
    dll.insert_at_end(450)
    dll.insert_at_end(550)
    print(f"Current List - \n\t {dll}")
    print(f"Length of List - {len(dll)}")

    # Insert before 200
    node_200 = dll.get_node(200)
    new_node = Node(123, None, None)
    dll.insert_before(new_node, node_200)

    # Insert after 200
    new_node = Node(225, None, None)
    dll.insert_after(new_node, node_200)
    print(f"Current List - \n\t {dll}")

    # Itertate through LL Nodes:
    for node in dll:
        print(f"{node.data}")

    dll.remove_from_beginning()
    dll.remove_from_beginning()
    dll.remove_from_end()
    dll.remove_from_end()
    print(f"Current List - \n\t {dll}")
    dll.remove_node(dll.get_node(350))
    print(f"Current List - \n\t {dll}")


if __name__ == "__main__":
    run_test_client()
