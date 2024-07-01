# Created by Sai at 6/23/2024

class BoundedMinHeap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self._heap = [0 for _ in range(self.capacity+1)]
        self._heap[0] = float("-inf")
        self.FRONT = 1

    def __parent(self, index):
        return index // 2

    def __left_child(self, index):
        return 2 * index

    def __right_child(self, index):
        return 2 * index + 1

    def __is_leaf(self, index):
        return 2*index > self.size

    def insert(self, key):
        if self.size >= self.capacity:
            return
        self.size += 1
        self._heap[self.size] = key

        current_index = self.size
        parent_index = self.__parent(current_index)
        while self._heap[current_index] < self._heap[parent_index]:
            self._heap[current_index], self._heap[parent_index] = self._heap[parent_index], self._heap[current_index]
            current_index = parent_index
            parent_index = self.__parent(current_index)

    def min_heapify(self, index):
        if not self.__is_leaf(index):
            left_child_index = self.__left_child(index)
            right_child_index = self.__right_child(index)
            if (self._heap[index] > self._heap[left_child_index]) or (self._heap[index] > self._heap[right_child_index]):
                if self._heap[left_child_index] < self._heap[right_child_index]:
                    self._heap[index], self._heap[left_child_index] = self._heap[left_child_index], self._heap[index]
                    self.min_heapify(left_child_index)
                else:
                    self._heap[index], self._heap[right_child_index] = self._heap[right_child_index], self._heap[index]
                    self.min_heapify(left_child_index)

    def extract_min(self):
        min_key = self._heap[self.FRONT]
        self._heap[self.FRONT] = self._heap[self.size]
        self.size -= 1
        self.min_heapify(self.FRONT)
        return min_key

    def get_min(self):
        if self.size == 0:
            return None
        return self._heap[self.FRONT]

    def __str__(self):
        return_string = ""
        for i in range(1, self.size+1):
            return_string += str(self._heap[i]) + ' '
        return return_string

    def __len__(self):
        return self.size


def run_test_client():
    min_heap = BoundedMinHeap(10)
    a = [18, 37, 88, 35, 99, 12, 3, 91, 5, 100]
    for elem in a:
        min_heap.insert(elem)
    print(min_heap)
    print(f"Get Minimum: {min_heap.extract_min()}")
    min_heap.insert(10)
    print(f"Get Minimum: {min_heap.extract_min()}")
    print(min_heap)
    print(f"Extract Minimum: {min_heap.extract_min()}")
    print(f"Extract Minimum: {min_heap.extract_min()}")
    print(f"Extract Minimum: {min_heap.extract_min()}")
    print(min_heap.size)
    print(min_heap)
    min_heap.insert(10)
    min_heap.insert(12)
    min_heap.insert(1)
    min_heap.insert(17)
    print(min_heap.size)
    print(min_heap)


if __name__ == "__main__":
    run_test_client()
