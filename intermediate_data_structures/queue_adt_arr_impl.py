# Created by Sai at 6/7/2024

class BoundedQueue:
    def __init__(self, capacity):
        self.arr = [None] * capacity
        self.head = 0
        self.tail = capacity - 1
        self.size = 0
        self.capacity = capacity

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, data_item):
        if self.is_full():
            print(f"Overflow!")
            return
        self.tail = (self.tail+1) % self.capacity
        self.arr[self.tail] = data_item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Empty Stack!")
            return
        data_item = self.arr[self.head]
        self.arr[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return data_item

    def peek_head(self):
        if self.is_empty():
            return None
        return self.arr[self.head]

    def peek_tail(self):
        if self.is_empty():
            return None
        return self.arr[self.tail]

    def __str__(self):
        queue_string = "Head:: "
        for item in self.arr:
            queue_string += str(item) + ' '
        queue_string += "::Tail"
        return queue_string


def run_test_client():
    queue = BoundedQueue(10)
    queue.enqueue(10)
    queue.enqueue(21)
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Dequeued: {queue.dequeue()}")
    print(queue)
    queue.enqueue(232)
    queue.enqueue(67)
    queue.enqueue(10)
    queue.enqueue(21)
    queue.enqueue(232)
    queue.enqueue(67)
    queue.enqueue(10)
    queue.enqueue(21)
    queue.enqueue(232)
    queue.enqueue(67)
    print(queue)
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Front: {queue.peek_head()}")
    print(f"Rear: {queue.peek_tail()}")
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Dequeued: {queue.dequeue()}")
    print(queue)


if __name__ == "__main__":
    run_test_client()
