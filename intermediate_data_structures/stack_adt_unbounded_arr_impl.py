# Created by Sai at 6/4/2024
import sys


class UnboundedStack:
    def __init__(self):
        self._arr = []

    def is_empty(self):
        return len(self._arr) == 0

    def push(self, elem):
        self._arr += [elem]

    def pop(self):
        if self.is_empty():
            print("Stack is Empty. Nothing to pop!")
        else:
            return self._arr.pop()

    def __str__(self):
        string_repr = ""
        for elem in self._arr:
            string_repr = str(elem) + " " + string_repr
        return string_repr

    def top_element(self):
        return self._arr[-1]

    def bottom_element(self):
        return self._arr[0]

    def __len__(self):
        return len(self._arr)


def main():
    stack = UnboundedStack()
    while True:
        input_elem = sys.stdin.readline().strip()
        if input_elem == '':
            break
        if input_elem.strip() == '-':
            print(stack.pop())
        else:
            stack.push(elem=input_elem)


def test_client():
    stack = UnboundedStack()
    print(f"Is Stack Empty: {stack.is_empty()}")
    stack.push("4:50")
    stack.push("from")
    stack.push("Paddington")
    stack.push("by")
    stack.push("Agatha")
    stack.push("Christie")
    print(f"Stack: Length: {len(stack)}")
    print(stack)
    stack.pop()
    stack.pop()
    print(f"Stack: Length: {len(stack)}")
    print(stack)
    stack.push("Miss")
    stack.push("Marple")
    print(f"stack: {stack}")
    print(f"Top Element: {stack.top_element()}")
    print(f"Bottom Element: {stack.bottom_element()}")
    print(f"popped: {stack.pop()}")
    print(f"popped: {stack.pop()}")
    print(f"popped: {stack.pop()}")
    print(f"Is Stack Empty: {stack.is_empty()}")
    print(f"popped: {stack.pop()}")
    print(f"popped: {stack.pop()}")
    print(f"popped: {stack.pop()}")
    print(f"popped: {stack.pop()}")
    print(f"popped: {stack.pop()}")
    print(f"Is Stack Empty: {stack.is_empty()}")





if __name__ == "__main__":
    test_client()
    # main()
