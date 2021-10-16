class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, item):
        self.s1.append(item)

    def dequeue(self):
        if len(self.s1) == 0:
            raise Exception("Cannot pop from empty queue")
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())
        item = self.s2.pop()
        while len(self.s2) >= 1:
            self.s1.append(self.s2.pop())
        return item


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
for i in range(5):
    print(queue.dequeue())