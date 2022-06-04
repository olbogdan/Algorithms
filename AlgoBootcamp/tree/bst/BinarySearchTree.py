class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, new_data):
        if self.data > new_data:
            if self.left is None:
                self.left = Node(new_data)
            else:
                self.left.insert(new_data)
        if self.data < new_data:
            if self.right is None:
                self.right = Node(new_data)
            else:
                self.right.insert(new_data)

    def contains(self, data):
        if self.data == data:
            return self
        if self.data > data and self.left:
            return self.left.contains(data)
        if self.data < data and self.right:
            return self.right.contains(data)
        return None

# insert() tests

node = Node(10)
node.insert(1)
assert node.left.data == 1

node = Node(10)
node.insert(1)
node.insert(-2)
assert node.left.left.data == -2

node = Node(10)
node.insert(1)
node.insert(5)
assert node.left.right.data == 5

node = Node(10)
node.insert(20)
assert node.right.data == 20

node = Node(10)
node.insert(20)
node.insert(30)
assert node.right.right.data == 30

# contains() tests

node = Node(10)
assert node.contains(1) is None

node = Node(10)
node.insert(1)
assert node.contains(1) is not None

node = Node(10)
node.insert(20)
node.insert(30)
assert node.contains(30) is not None



