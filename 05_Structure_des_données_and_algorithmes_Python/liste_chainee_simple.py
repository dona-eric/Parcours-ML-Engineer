
# definir la classe Noeud
class Node:
    def __init__(self, data):
        self.value = data
        self.next = None


# definir la classe ListeChainee
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_begining(self, data):
        new_node = Node(data)
        # Check whether the linked list has a head node
        if self.head:
            # point the new node's next to the current head
            # and update the head to be the new node
            new_node.next = self.head
            self.head = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def remove_at_begining(self):
            # The "next" node of the head becomes the new head node
            self.head = self.head.next