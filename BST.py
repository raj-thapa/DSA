# This is the binary search tree algorithm

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root

        while True:

            if value < temp.value:
                if temp.left is not None:
                    temp = temp.left
                else:
                    temp.left = new_node
                    return True
            elif value > temp.value:
                if temp.right is not None:
                    temp = temp.right
                else:
                    temp.right = new_node
                    return True
            else:
                return False

    def contains(self, value):
        if self.root == None:
            return False
        temp = self.root

        while True:
            if temp.value == value:
                return True
            if value < temp.value:
                if temp.left is not None:
                    temp = temp.left
                else:
                    return False
            if value > temp.value:
                if temp.left is not None:
                    temp = temp.right
                else:
                    return False
