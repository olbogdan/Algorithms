class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, value):
        self.head = self.Node(value, self.head)

    def add_last(self, value):
        last = self._get_last_node()
        next = self.Node(value, None)
        if last:
            last.next = next
        else:
            self.head = next

    def get_first(self):
        return self.head.data if self.head else None

    def get_first_node(self):
        return self.head

    def _get_last_node(self):
        node = self.head
        last = self.head
        while node:
            last = node
            node = node.next
        return last

    def get_last(self):
        last = self._get_last_node()
        return last.data if last else None

    def remove_first(self):
        if self.head:
            self.head = self.head.next

    def remove_last(self):
        if self.head is None:
            return
        if self.size() == 1:
            self.clear()
            return

        node = self.head
        while node.next and node.next.next:
            node = node.next
        node.next = None

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size

    def clear(self):
        self.head = None

    def remove_at(self, index):
        if index == 0 and self.head:
            self.head = self.head.next
        prev_node = self._get_at(index-1)
        if prev_node and prev_node.next:
            item_to_remove = prev_node.next
            prev_node.next = item_to_remove.next

    def insert_at(self, index, value):
        # newNode = self.Node(value, None)
        if self.size() < (index + 1):
            self.add_last(value)
        elif index == 0:
            self.add_first(value)
        else:
            prev = self._get_at(index-1)
            next = prev.next
            new_node = self.Node(value, next)
            prev.next = new_node

    # returns a node for internal usage
    def _get_at(self, index):
        node = self.head
        position = 0
        while node:
            if position == index:
                return node
            position += 1
            node = node.next
        return None

    def get_at(self, index):
        node = self._get_at(index)
        return node.data if node else None

    def __repr__(self):
        represent = []
        node = self.head
        while node is not None:
            represent.append(node.data)
            node = node.next
        return str(represent)

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    class Node:
        def __init__(self, data, next):
            self.data = data
            self.next = next

        def __repr__(self):
            return str(self.data)


list = LinkedList()
assert list.size() == 0
assert list.get_first() is None
assert list.get_last() is None

list.add_first("a")
list.add_first("b")
list.add_first("c")
list.add_first("d")

assert list.size() == 4
assert list.get_first() == "d"
assert list.get_last() == "a"

list.remove_first()
assert list.get_first() == "c"

assert list.get_last() == "a"
list.remove_last()
assert list.get_last() == "b"

list.add_last("y")
assert list.get_last() == "y"

list.clear()
assert list.size() == 0

list.add_last("y")
assert list.get_last() == "y"
assert list.get_first() == "y"

list = LinkedList()
list.add_first("a")
list.add_first("b")
list.add_first("c")
assert list.get_at(2) == "a"


# test remove at index
list = LinkedList()
list.add_first("a")
list.add_first("b")
list.add_first("c")
list.add_first("d")
assert list.get_at(0) == "d"
list.remove_at(0)
assert list.get_at(0) == "c"
assert list.get_at(1) == "b"
list.remove_at(1)
assert list.get_at(1) == "a"
list.remove_at(0)
list.remove_at(0)
list.remove_at(0)
assert list.size() == 0

# test insert at index
list = LinkedList()
list.insert_at(0, "a")
assert list.get_at(0) == "a"

list = LinkedList()
list.insert_at(5, "a")
assert list.get_at(0) == "a"

list = LinkedList()
list.add_last("a")
list.add_last("b")
list.add_last("c")
list.add_last("d")
list.insert_at(0, "x")
assert list.get_at(0) == "x"

list = LinkedList()
list.add_last("a")
list.add_last("b")
list.add_last("c")
list.add_last("d")
list.insert_at(2, "x")
assert list.get_at(2) == "x"

list = LinkedList()
list.add_last("a")
for i in list:
    assert i == "a"
