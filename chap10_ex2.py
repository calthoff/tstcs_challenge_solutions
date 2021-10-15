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
        return current.next

    def create_list(self, n, create_cycle=False):
        node = None
        for i in range(2, n):
            node = self.append(i)
        if create_cycle:
            if node:
                node.next = self.head

    def contains_cycle(self):
        slow = self.head
        fast = self.head
        while True:
            try:
                slow = slow.next
                fast = fast.next.next
                if slow is fast:
                    return True
            except:
                return False


linked_list_one = LinkedList()
linked_list_one.create_list(100)
linked_list_two = LinkedList()
linked_list_two.create_list(100, True)



print(linked_list_one.contains_cycle())
print(linked_list_two.contains_cycle())