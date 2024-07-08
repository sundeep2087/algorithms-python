# Created by Sai at 6/11/2024

from intermediate_data_structures.queue_adt_node_implementation import LLQueue
from intermediate_data_structures.stack_adt_linked_list_impl import Stack
import numpy as np
import time


# def reverse_k_elements(input_queue, k_value):
#     if k_value == 0:
#         return
#     curr_elem = input_queue.dequeue()
#     reverse_k_elements(input_queue, k_value-1)
#     input_queue.enqueue(curr_elem)
#
#
# def generate_updated_queue(input_queue, k_value):
#     reverse_k_elements(input_queue, k_value)
#     rem_len = abs(input_queue.queue_size - k_value)
#     for i in range(rem_len):
#         curr_elem = input_queue.dequeue()
#         input_queue.enqueue(curr_elem)
#     return input_queue


# My Own Implementation - Uses Auxiliary Stack.
# No problem of maximum recursion depth exceeded

def reverse_k_elements(input_queue, k_value):
    rem_queue_size = abs(input_queue.size() - k_value)
    aux_stack = Stack()
    while k_value > 0:
        aux_stack.push(input_queue.dequeue())
        k_value -= 1
    while not aux_stack.is_empty():
        input_queue.enqueue(aux_stack.pop())
    for i in range(rem_queue_size):
        front_elem = input_queue.dequeue()
        input_queue.enqueue(front_elem)
    return input_queue


def run_test_client():
    test_lists = [
        np.random.randint(1, 999, 10),
        np.random.randint(1, 999, 20),
        np.random.randint(1, 999, 15),
        np.random.randint(1, 99, 50),
        np.random.randint(0, 5, 10),
        np.random.randint(0, 2, 10)
    ]
    k_list = [6, 12, 7, 30, 5, 4]
    print(f"*" * 100)
    for lst, k_value in zip(test_lists, k_list):
        queue1 = LLQueue()
        for i in lst:
            queue1.enqueue(i)
        print(f"Original Queue: \n\t {queue1}")
        updated_list = reverse_k_elements(queue1, k_value)
        print(f"Updated List: \n\t {updated_list}")
        print(f"*" * 100)

    # Testing with large number of elements
    print(f"Testing with large input range.")
    queue1 = LLQueue()
    elements_list = list(np.random.randint(0, 999, 10000000))
    for i in elements_list:
        queue1.enqueue(i)
    print(f"Reversing Started!")
    start_time = time.time()
    updated_list = reverse_k_elements(queue1, 10000)
    print(f"Reversing Completed! Time Elapsed: {(time.time() - start_time):.2f} secs.")
    print(f"*" * 100)


if __name__ == "__main__":
    run_test_client()