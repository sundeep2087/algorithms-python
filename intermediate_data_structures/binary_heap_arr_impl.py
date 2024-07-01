# Created by Sai at 6/22/2024

class BinaryHeap:
    def __init__(self):
        self._heap = []

    def is_empty(self):
        return len(self._heap) == 0

    def insert(self, key):
        self._heap.append(key)
        self.__sift_up(len(self._heap) - 1)

    def __sift_up(self, index):
        parent_index = (index - 1) // 2
        while parent_index >= 0 and self._heap[index] < self._heap[parent_index]:
            self._heap[index], self._heap[parent_index] = self._heap[parent_index], self._heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def __sift_down(self, index):
        left_child_index = 2*index + 1
        right_child_index = 2*index + 2
        smallest_key_index = index
        if left_child_index < len(self._heap) and self._heap[left_child_index] < self._heap[smallest_key_index]:
            smallest_key_index = left_child_index
        if right_child_index < len(self._heap) and self._heap[right_child_index] < self._heap[smallest_key_index]:
            smallest_key_index = right_child_index
        if smallest_key_index != index:
            self._heap[smallest_key_index], self._heap[index] = self._heap[index], self._heap[smallest_key_index]
            self.__sift_down(smallest_key_index)

    def extract_min(self):
        if self.is_empty():
            return None

        min_key = self._heap[0]
        self._heap[0] = self._heap[-1]
        self._heap.pop()
        self.__sift_down(0)

        return min_key

    def get_min(self):
        if self.is_empty():
            return None

        return self._heap[0]

    def __str__(self):
        return_string = ""
        for key in self._heap:
            return_string += str(key) + ' '
        return return_string


def run_test_client():
    min_heap = BinaryHeap()
    a = [101, 387, 191, 473, 181, 393, 192, 233, 271, 393]
    for elem in a:
        min_heap.insert(elem)
    print(f"Get Minimum: {min_heap.get_min()}")
    min_heap.insert(10)
    print(f"Get Minimum: {min_heap.get_min()}")
    print(min_heap)
    print(f"Extract Minimum: {min_heap.extract_min()}")
    print(f"Extract Minimum: {min_heap.extract_min()}")
    print(f"Extract Minimum: {min_heap.extract_min()}")
    print(min_heap)


if __name__ == "__main__":
    run_test_client()