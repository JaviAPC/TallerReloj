class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleCircularList:
    def __init__(self):
        self.first = None

    def insert(self, valor):
        new_node = Node(valor)
        if self.first is None:
            self.first = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last_node = self.first.prev
            last_node.next = new_node
            new_node.prev = last_node
            new_node.next = self.first
            self.first.prev = new_node

    def advance(self, current_node):
        return current_node.next

    def back(self, current_node):
        return current_node.prev