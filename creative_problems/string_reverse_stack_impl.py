# Created by Sai at 6/9/2024

from elementary_data_structures.stack_adt_linked_list_impl import Stack


def reverse_string(input_string):
    stack = Stack()
    for charac in input_string:
        stack.push(charac)

    return_string = ""
    for element in stack:
        return_string += element

    return return_string.strip()


def run_test_client():
    input_strings = ["Blue Headphones", "200mg Advil", "liril", "malayalam"]
    for in_str in input_strings:
        reversed_string = reverse_string(in_str)
        print(reversed_string)


if __name__ == "__main__":
    run_test_client()