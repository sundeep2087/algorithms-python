# Created by Sai at 6/7/2024

class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data_element):
        new_node = Node(data_element, None)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            print(f"Empty Stack! No elements to pop.")
            return
        curr_node = self.head
        popped_element = curr_node.data
        if curr_node.next is None:
            self.head = None
        else:
            self.head = curr_node.next
        return popped_element

    def peek(self):
        if self.head is None:
            print("Stack is Empty!")
            return
        return self.head.data

    def is_empty(self):
        return self.head is None

    class StackIterator:
        def __init__(self, curr_node):
            self.curr_node = curr_node

        def __iter__(self):
            return self

        def __next__(self):
            if self.curr_node:
                curr_data = self.curr_node.data
                self.curr_node = self.curr_node.next
                return curr_data
            else:
                raise StopIteration

    def __iter__(self):
        return self.StackIterator(self.head)

    def __str__(self):
        curr_node = self.head
        stack_data = ""
        while curr_node is not None:
            data_item = curr_node.data
            stack_data += str(data_item) + "\n"
            curr_node = curr_node.next
        return stack_data


def run_test_client():
    stack = Stack()
    stack.push(10)
    stack.push(298)
    stack.push("Halo")
    stack.push(234)
    stack.push(89)
    stack.push("Hi")
    stack.push("Hello")
    print(stack)
    print("\n\n")
    for data in stack:
        print(data)
    stack.pop()
    stack.pop()
    print("\n\n")
    print(stack)
    print(f"stack.peek(): {stack.peek()}")
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    print("\n\n")
    print(stack)


if __name__ == "__main__":
    run_test_client()
