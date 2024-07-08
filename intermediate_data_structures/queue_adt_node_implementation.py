# Created by Sai at 6/7/2024

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LLQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.queue_size = 0

    def is_empty(self):
        return self.head is None

    def enqueue(self, data_item):
        new_node = Node(data_item, None)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.queue_size += 1
            return
        self.tail.next = new_node
        self.tail = new_node
        self.queue_size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        removed_item = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.queue_size -= 1
        return removed_item

    def __str__(self):
        query_string = "front:: "
        curr_node = self.head
        while curr_node is not None:
            query_string += str(curr_node.data) + " "
            curr_node = curr_node.next
        query_string += "::rear"
        return query_string

    def size(self):
        return self.queue_size

    def get_front(self):
        if self.is_empty():
            return None
        return self.head.data

    def get_rear(self):
        if self.is_empty():
            return None
        return self.tail.data

    class QueueIterator:
        def __init__(self, curr_node):
            self.curr_node = curr_node

        def __iter__(self):
            return self

        def __next__(self):
            if self.curr_node:
                curr_data = self.curr_node.data
                self.curr_node = self.curr_node.next
                return curr_data
            else:
                raise StopIteration

    def __iter__(self):
        return self.QueueIterator(self.head)


def run_test_client():
    queue = LLQueue()
    print(f"Is Queue Empty: {queue.is_empty()}")
    queue.enqueue(1021)
    queue.enqueue(341)
    queue.enqueue(6421)
    queue.enqueue(6721)
    print('*' * 10)
    for element in queue:
        print(element)
    print('*' * 10)
    print(queue.size())
    print(f"Front Element: {queue.get_front()}")
    print(queue.dequeue())
    print(f"{queue}")
    print(queue.dequeue())
    print(f"{queue}")
    print(queue.dequeue())
    print(f"{queue}")
    print(queue.dequeue())
    print(queue.dequeue())
    print(f"{queue}")


if __name__ == "__main__":
    run_test_client()