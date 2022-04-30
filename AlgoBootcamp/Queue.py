from collections import deque


class Queue:
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


def weave(source_one: Queue, source_two: Queue):
    q = Queue()
    while source_one.peek() is not None or source_two.peek() is not None:
        if source_one.peek() is not None:
            q.add(source_one.remove())
        if source_two.peek() is not None:
            q.add(source_two.remove())
    return q


q1 = Queue()
q1.add("a")
q1.add("b")
q1.add("c")
q1.add("d")
q1.add("e")
q1.add("f")
q2 = Queue()
q2.add(1)
q2.add(2)
q2.add(3)
result = weave(q1, q2)
while result.peek() is not None:
    print(result.remove())
