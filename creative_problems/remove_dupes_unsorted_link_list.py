# Created by Sai at 6/9/2024
import numpy as np


from elementary_data_structures.oneway_linked_list_implementation import LinkedList


def remove_duplicates(unsorted_list):
    elements_counts_dict = {}
    for item in unsorted_list:
        if item not in list(elements_counts_dict.keys()):
            elements_counts_dict[item] = 1
        else:
            unsorted_list.remove_node(item)

    return unsorted_list


def run_test_client():
    for i in range(3):
        list1 = np.random.randint(1, 10, 7)
        print(f"Original List: {list1}")
        linked_list = LinkedList()
        for item in list1:
            linked_list.insert_at_beginning(item)
        deduped_list = remove_duplicates(linked_list)
        print(f"De-duped List: {deduped_list}")


if __name__ == "__main__":
    run_test_client()