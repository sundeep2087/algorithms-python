# Created by Sai at 6/9/2024

from intermediate_data_structures.stack_adt_linked_list_impl import Stack


def check_balanced_brackets(input_expression):
    bracket_stack = Stack()
    for input_char in input_expression:
        if input_char in ['(', '{', '[']:
            bracket_stack.push(input_char)
        elif input_char in [']', '}', ')']:
            stack_top_elem = None
            if not bracket_stack.is_empty():
                stack_top_elem = bracket_stack.pop()
            if input_char == ']' and stack_top_elem != '[':
                return -1
            if input_char == '}' and stack_top_elem != '{':
                return -1
            if input_char == ')' and stack_top_elem != '(':
                return -1

    if not bracket_stack.is_empty():
        return -1

    return 0


def run_test_client():
    test_strings = ["[{()}([]{()()})]", "{[}]", "(){}[([)]]", "{{{{[[[[(((())))]]]]}}}}[[]]"]
    for test_str in test_strings:
        result = check_balanced_brackets(test_str)
        if result == -1:
            print(f"Unbalanced!")
        else:
            print("Balanced!")


if __name__ == "__main__":
    run_test_client()
