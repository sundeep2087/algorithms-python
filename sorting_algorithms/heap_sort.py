# Created by Sai at 6/26/2024
from intermediate_data_structures.min_heap_arr_impl import MinHeap


def max_heapify(arr, n, i):
    left_child_i = 2 * i + 1
    right_child_i = 2 * i + 2
    largest_key_i = i

    if left_child_i < n and arr[left_child_i] > arr[largest_key_i]:
        largest_key_i = left_child_i
    if right_child_i < n and arr[right_child_i] > arr[largest_key_i]:
        largest_key_i = right_child_i
    if largest_key_i != i:
        arr[largest_key_i], arr[i] = arr[i], arr[largest_key_i]
        max_heapify(arr, n, largest_key_i)


def heap_sort(arr):
    # Method 1 : Using Unbounded minheap - not an inplace manipulation
    # min_heap = MinHeap()
    # for elem in arr:
    #     min_heap.insert(elem)
    #
    # for i in range(len(arr), 1, -1):
    #     extracted_min = min_heap.extract_min()
    #     print(extracted_min, end=" ")
    # print("=" * 150)

    # Method 2 : Using Bounded Maxheap - Inplace Sorting
    for i in range(len(arr)//2-1, -1, -1):
        max_heapify(arr, len(arr), i)

    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)


def run_test_client():
    test_lists = [
        [20, 25, 54, 65, 40, 76, 3, 53, 99, 98],
        [996, 77, 969, 423, 833, 71, 29, 472, 856, 8],
        [529, 923, 173, 261, 929, 508, 910, 131, 469, 48, 113, 885, 485,
         659, 383, 67, 510, 663, 920, 210, 328, 135, 236, 483, 23, 954,
         48, 665, 134, 360, 998, 636, 830, 493, 344, 22, 512, 913, 949,
         127, 559, 661, 178, 772, 365, 817, 164, 553, 103, 489, 384, 894,
         288, 903, 941, 638, 682, 15, 84, 688, 924, 662, 382, 710, 345,
         290, 195, 776, 561, 760, 917, 289, 364, 60, 354, 684, 735, 402,
         86, 10, 405, 408, 382, 773, 190, 212, 489, 996, 843, 28, 703,
         865, 160, 875, 534, 247, 105, 786, 679, 455],
        [51827, 36093, 6596, 13586, 66990, 73379, 82486, 61558, 7136,
         13348, 47119, 78885, 73790, 91976, 63159, 24024, 48341, 23297,
         2503, 636, 36282, 13495, 38326, 60527, 17028, 38147, 63636,
         33641, 47556, 77829, 34905, 68401, 82216, 7327, 44957, 94331,
         24964, 57703, 17662, 10348, 30308, 35487, 58001, 42721, 5062,
         51801, 96638, 27074, 43088, 35018, 37100, 26582, 5987, 79947,
         83020, 91555, 18513, 30288, 514, 5621, 78691, 92683, 21557,
         85134, 16679, 68539, 98635, 82379, 75868, 53636, 52696, 50604,
         91647, 91338, 6355, 30792, 65279, 65767, 16121, 37312, 1984,
         31807, 34429, 35336, 94, 10051, 41117, 91072, 32260, 6714,
         73212, 37573, 75536, 70685, 75476, 45158, 34202, 99569, 11679,
         2004]
    ]
    for test_list_i in test_lists:
        heap_sort(test_list_i)
        print(test_list_i)
        print("=" * 150)


if __name__ == "__main__":
    run_test_client()