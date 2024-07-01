# Created by Sai at 6/9/2024


def count_spaces(input_string):
    input_string_list = input_string.split(" ")
    spaces_count = len(input_string_list) - 1
    return spaces_count


def run_test_client():
    input_strings = [
        "I was asked how to find middle node in Linked list.",
        "a        b",
        "                 ",
        "     After first question, they asked how to delete node in Linked list without head node.",
        "After dsa round they started asking me questions from my resume and projects  .   "
    ]
    for in_str in input_strings:
        count_of_spaces = count_spaces(in_str)
        print(f"{count_of_spaces}")


if __name__ == "__main__":
    run_test_client()