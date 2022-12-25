class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp != None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head= new_node
            self.tail= new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
        self.length += 1
        return True
        
    def pop(self):
        if self.head == None:
            return None
            
        temp = self.head
        pre = self.head
        
        while(temp.next != None):
            pre = temp
            temp = temp.next
                    
        self.tail = pre
        self.tail.next = None
        if self.length == 1:
            self.head = None
            self.tail = None
        self.length -= 1
        return temp
        
    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            self.head = new_node
            self.head.next = temp
            
        self.length += 1
        return True
        
    def pop_first(self):
        if self.head == None:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else: 
            self.head = self.head.next
            temp.next = None
        self.length -= 1
        return temp
            
my_linkedlist = LinkedList(1)

my_linkedlist.pop()
my_linkedlist.prepend(2)
my_linkedlist.print_list()
















