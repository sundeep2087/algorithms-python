# Created by Sai at 7/7/2024
from intermediate_data_structures.stack_adt_unbounded_arr_impl import UnboundedStack


class Queue:
    def __init__(self):
        self.stack1 = UnboundedStack()
        self.stack2 = UnboundedStack()

    def enqueue(self, key):
        self.stack1.push(key)

    def dequeue(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return None
        if len(self.stack2) == 0:
            for _ in range(len(self.stack1)):
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def __len__(self):
        return len(self.stack1) + len(self.stack2)


def run_test_client():
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(21)
    print(f"Length of Queue: {len(queue)}")
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Length of Queue: {len(queue)}")
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
    print(f"Length of Queue: {len(queue)}")
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Length of Queue: {len(queue)}")


if __name__ == "__main__":
    run_test_client()