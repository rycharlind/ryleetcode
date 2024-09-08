class Node:
    def __init__(self, data):
        self.data = data  # The data value of the node
        self.next = None  # Reference to the next node in the list

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    # Adds a new node with the specified data at the end of the list.
    def append(self, data):
        new_node = Node(data)

        # If the list is empty (self.head is None), the new node becomes the head of the list.
        if not self.head:
            self.head = new_node
            return
        
        # If the list is not empty:
        # iterate through the nodes until it finds the last node (where last.next is None) 
        # and set its next reference to the new node.
        last = self.head
        while last.next: # starts a while loop that continues as long as last.next is not None.
            last = last.next
        
        last.next = new_node

    # Adds a new node with the specified data at the beginning of the list.
    def prepend(self, data):
        new_node = Node(data)
        
        new_node.next = self.head # The new node's next reference is set to the current head of the list.
        self.head = new_node

    def delete_with_value(self, data):
        # List is empty, nothing to delete
        if not self.head:
            return
        
        # data is at the head, so make the new head the next node.
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            
            current = current.next

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)

def test_linked_list():
    ll = LinkedList()
    ll.prepend("hello")
    ll.prepend("world")
    ll.display()