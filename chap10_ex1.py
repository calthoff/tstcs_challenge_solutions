class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def print_list(self):
        current = self.head
        while current.next:
            current = current.next
            print(current.data)

linked_list = LinkedList()

for i in range(101):
    linked_list.append(i)

linked_list.print_list()
