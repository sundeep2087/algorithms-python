# Created by Sai at 6/4/2024

class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data_element):
        new_node = Node(data_element, None)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data_element):
        new_node = Node(data_element, None)
        if self.head is None:
            self.head = new_node
            return
        else:
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = new_node

    def insert_at_index(self, data_element, index_position):
        new_node = Node(data_element, None)
        curr_node = self.head
        curr_position = 0
        if index_position == curr_position:
            self.insert_at_beginning(data_element)
        else:
            while curr_node is not None and curr_position+1 != index_position:
                curr_position += 1
                curr_node = curr_node.next

            if curr_node is not None:
                new_node.next = curr_node.next
                curr_node.next = new_node
            else:
                print(f"Index Position {index_position} is not available in the Linked List")

    def remove_first_node(self):
        if self.head is None:
            print(f"Linked list empty, no elements to remove!")
            return
        else:
            self.head = self.head.next

    def remove_last_node(self):
        if self.head is None:
            print(f"Linked list empty, no elements to remove!")
            return
        else:
            curr_node = self.head
            while curr_node.next.next is not None:
                curr_node = curr_node.next
            curr_node.next = None

    def remove_at_index(self, index_position):
        if self.head is None:
            print(f"Linked list empty, no elements to remove!")
            return
        else:
            curr_position = 0
            curr_node = self.head
            if curr_position+1 == index_position:
                self.remove_first_node()
            else:
                while curr_node is not None and curr_position+1 != index_position:
                    curr_position += 1
                    curr_node = curr_node.next

                if curr_node is None:
                    print("Index not present!")
                else:
                    curr_node.next = curr_node.next.next

    def remove_node(self, data_element):
        if self.head is None:
            print("Empty list! Nothing to remove.")
        else:
            curr_node = self.head

            if curr_node.data == data_element:
                self.remove_first_node()
                return

            while curr_node.next is not None and curr_node.next.data != data_element:
                curr_node = curr_node.next

            if curr_node.next is None:
                print(f"Node Unavailable!")
            else:
                curr_node.next = curr_node.next.next


    def update_node(self, new_data_element, index_position):
        curr_node = self.head
        curr_position = 0

        if curr_position == index_position:
            curr_node.data = new_data_element
        else:
            while curr_node.next is not None and curr_position+1 != index_position:
                curr_node = curr_node.next
                curr_position += 1

            if curr_node is None:
                print(f"Index position unavailable!")
            else:
                curr_node.data = new_data_element

    def __str__(self):
        curr_node = self.head
        ll_string = ''
        while curr_node is not None:
            ll_string += str(curr_node.data) + ' '
            curr_node = curr_node.next
        return ll_string

    def __len__(self):
        if self.head == None:
            return 0
        else:
            ll_length = 0
            curr_node = self.head
            while curr_node is not None:
                ll_length += 1
                curr_node = curr_node.next
        return ll_length

    class LLIterator:
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
        return self.LLIterator(self.head)


def run_test_client():
    linked_list1 = LinkedList()
    linked_list1.insert_at_beginning("The")
    linked_list1.insert_at_beginning("quick")
    linked_list1.insert_at_beginning("brown")
    linked_list1.insert_at_end("fox")
    linked_list1.insert_at_end("jumped")
    linked_list1.insert_at_index("over", 3)
    print(len(linked_list1))
    linked_list1.update_node('the', 3)
    ll_string = ''
    for data_element in linked_list1:
        ll_string += str(data_element) + ' '
    print(ll_string)
    linked_list1.remove_first_node()
    linked_list1.remove_last_node()
    linked_list1.remove_node('over')
    linked_list1.remove_at_index(1)
    print(linked_list1)
    linked_list1.remove_last_node()
    print(linked_list1)



if __name__ == "__main__":
    run_test_client()

