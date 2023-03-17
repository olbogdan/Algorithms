from collections import deque

# Implement a Queue datastructure using two Stacks
class QueueFromStack:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def add(self, value):
        self.stack1.push(value)

    def remove(self):
        if self.stack2.peek() is None:
            while self.stack1:
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        if self.stack2.peek() is None:
            while self.stack1:
                self.stack2.push(self.stack1.pop())
        return self.stack2.peek()

# Task: Implement a Stack using a deque
class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None


# Task: Implement a Queue using a deque
class QueueDeq:
    def __init__(self):
        self.queue = deque()

    def add(self, record):
        self.queue.appendleft(record)

    def remove(self):
        return self.queue.pop()

    def peek(self):
        if self.queue:
            return self.queue[-1]
        else:
            return None


# Task: Implement a Queue using an array
class Queue2:
    def __init__(self):
        self.queue = []

    # (O)n
    def add(self, record):
        self.queue.insert(0, record)

    def remove(self):
        return self.queue.pop()

    def peek(self):
        if self.queue:
            return self.queue[-1]
        else:
            return None


# Task: Implement zipper of two Queues
def weave(source_one: QueueDeq, source_two: QueueDeq):
    q = QueueDeq()
    while source_one.peek() is not None or source_two.peek() is not None:
        if source_one.peek() is not None:
            q.add(source_one.remove())
        if source_two.peek() is not None:
            q.add(source_two.remove())
    return q


q1 = QueueDeq()
q1.add("a")
q1.add("b")
q1.add("c")
q1.add("d")
q1.add("e")
q1.add("f")
q2 = QueueDeq()
q2.add(1)
q2.add(2)
q2.add(3)
result = weave(q1, q2)
while result.peek() is not None:
    print(result.remove())
