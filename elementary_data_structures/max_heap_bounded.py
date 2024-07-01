# Created by Sai at 6/23/2024

class BoundedMaxHeap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self._heap = [0.0 for i in range(self.capacity + 1)]
        self._heap[0] = float("inf")
        self.FRONT = 1

    def parent(self, index):
        return index // 2

    def left_child(self, index):
        return 2 * index

    def right_child(self, index):
        return 2 * index + 1

    def is_leaf(self, index):
        return 2 * index > self.size

    def swap(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def insert(self, key):
        if self.size >= self.capacity:
            return
        self.size += 1
        self._heap[self.size] = key

        current_index = self.size
        parent_index = self.parent(current_index)

        while self._heap[parent_index] < self._heap[current_index]:
            self._heap[current_index], self._heap[parent_index] = self._heap[parent_index], self._heap[current_index]
            current_index = parent_index
            parent_index = self.parent(current_index)

    def max_heapify(self, index):
        if not self.is_leaf(index):
            left_node_index = self.left_child(index)
            right_node_index = self.right_child(index)
            if (self._heap[index] < self._heap[left_node_index]) or (self._heap[index] < self._heap[right_node_index]):
                if self._heap[left_node_index] > self._heap[right_node_index]:
                    self._heap[index], self._heap[left_node_index] = self._heap[left_node_index], self._heap[index]
                    self.max_heapify(left_node_index)
                else:
                    self._heap[index], self._heap[right_node_index] = self._heap[right_node_index], self._heap[index]
                    self.max_heapify(right_node_index)

    def extract_max(self):
        max_key = self._heap[self.FRONT]
        self._heap[self.FRONT] = self._heap[self.size]
        self.size -= 1
        self.max_heapify(self.FRONT)
        return max_key

    def get_max(self):
        if self.size == 0:
            return
        return self._heap[self.FRONT]

    def __str__(self):
        return_string = ""
        for i in range(1, self.size + 1):
            return_string += str(self._heap[i]) + ' '
        return return_string

    def __len__(self):
        return self.size


def run_test_client():
    max_heap = BoundedMaxHeap(8)
    print(f"Heap Size: {len(max_heap)}")
    max_heap.insert(34)
    max_heap.insert(37)
    max_heap.insert(11)
    max_heap.insert(93)
    print(f"Heap Size: {len(max_heap)}")
    max_heap.insert(66)
    max_heap.insert(25)
    max_heap.insert(83)
    max_heap.insert(92)
    max_heap.insert(79)
    max_heap.insert(49)
    print(f"Heap: {max_heap}")
    print(f"Heap Size: {len(max_heap)}")
    print(f"Current Max: {max_heap.get_max()}")
    print(f"Extracted Max: {max_heap.extract_max()}")
    print(f"Extracted Max: {max_heap.extract_max()}")
    print(f"Heap: {max_heap}")


if __name__ == "__main__":
    run_test_client()