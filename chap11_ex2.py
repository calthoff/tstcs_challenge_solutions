class MaxStack():
    def __init__(self):
        self.stack = []
        self.max = []

    def push(self, n):
        if len(self.stack) < 1:
            self.max.append(n)
        elif n >= self.max[-1]:
            self.max.append(n)
        else:
            self.max.append(self.stack[-1])
        self.stack.append(n)

    def pop(self):
        self.max.pop()
        return self.stack.pop()

    def get_max(self):
        return self.max[-1]


max_stack = MaxStack()
max_stack.push(18)
print(max_stack.get_max())
max_stack.push(122)
print(max_stack.get_max())
max_stack.push(11)
print(max_stack.get_max())
max_stack.push(14)

