# Created by Sai at 6/11/2024

class Node:
    def __init__(self, data, next_link, prev_link):
        self.data = data
        self.next = next_link
        self.prev = prev_link


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.deque_size = 0

    def is_empty(self):
        return self.head is None

    def size(self):
        return self.deque_size

    def push_left(self, data_item):
        new_node = Node(data_item, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.deque_size += 1
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        self.deque_size += 1

    def push_right(self, data_item):
        new_node = Node(data_item, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.deque_size += 1
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.deque_size += 1

    def pop_left(self):
        if self.head is None:
            return None

        if self.deque_size == 1:
            return_data = self.head.data
            self.head = None
            self.tail = None
        else:
            return_data = self.head.data
            next_head = self.head.next
            next_head.prev = None
        self.deque_size -= 1
        return return_data

    def pop_right(self):
        if self.head is None:
            return None

        if self.deque_size == 1:
            return_data = self.head.data
            self.head = None
            self.tail = None
        else:
            return_data = self.tail.data
            next_tail = self.tail.prev
            next_tail.next = None
        self.deque_size -= 1
        return return_data

    def __str__(self):
        curr_node = self.head
        return_string = "Left::>> "
        while curr_node is not None:
            return_string += str(curr_node.data) + " "
            curr_node = curr_node.next
        return_string += "<<::Right"
        return return_string


def run_test_client():
    deque = Deque()
    deque.push_right(10)
    deque.push_right(20)
    deque.push_left(40)
    deque.push_left(30)
    print(deque)
    print(f"Deque Size: {deque.size()}")
    print(f"Is deque empty?: {deque.is_empty()}")
    deque.pop_left()
    deque.pop_right()
    print(deque)
    deque.pop_left()
    deque.pop_right()
    print(f"Deque Size: {deque.size()}")
    print(f"Is deque empty?: {deque.is_empty()}")


if __name__ == "__main__":
    run_test_client()







