class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None

    def push_back(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
        else:
            crawler = self.root
            while crawler.next:
                crawler = crawler.next
            crawler.next = new_node

    def traverse(self):
        crawler = self.root
        while crawler:
            print(crawler.data, end=" ")
            crawler = crawler.next
        print()

    class Iterator:
        def __init__(self, current_node):
            self.current_node = current_node

        def __iter__(self):
            return self

        def __next__(self):
            if self.current_node:
                data = self.current_node.data
                self.current_node = self.current_node.next
                return data
            else:
                raise StopIteration

    def __iter__(self):
        return self.Iterator(self.root)


# Driver program
if __name__ == "__main__":
    linked_list = LinkedList()

    # Add few items to the end of LinkedList
    linked_list.push_back(1)
    linked_list.push_back(2)
    linked_list.push_back(3)

    print("Traversing LinkedList through method")
    linked_list.traverse()

    print("Traversing LinkedList through Iterator")
    for item in linked_list:
        print(item, end=" ")
    print()
