class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_first(self,value):
        new_node = Node(value)

        if self.head == None:
            return new_node
        
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self,value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            return new_node

        current = self.head
        while current.next :
            current= current.next
        
        current.next = new_node

    def insert_after_k(self, value, k):
        new_node = Node(value)
        current = self.head
        
        #If there are no nodes in the linked list
        #Set the new node as head and return
        if current is None:
            self.head = new_node
            return
        
        #Iterate to the k-th node
        for _ in range(k-1):
            current = current.next
        # Set the next of new Node to next of current
        new_node.next = current.next
        
        #Set the next of current to new Node
        current.next = new_node