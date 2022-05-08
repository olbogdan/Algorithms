class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add(self, data):
        self.children.append(Node(data))

    def remove(self, data):
        i = 0
        while i < len(self.children):
            if self.children[i].data == data:
                del self.children[i]
            else:
                i += 1

    def __repr__(self):
        return self.data


# Test Add()
node = Node("X")
node.add("A")
node.add("B")
node.add("C")
assert len(node.children) == 3
assert node.children[0].data == "A"

# Test Remove()
node = Node("X")
node.add("A")
node.add("B")
assert len(node.children) == 2
node.remove("A")
assert len(node.children) == 1
assert node.children[0].data == "B"
