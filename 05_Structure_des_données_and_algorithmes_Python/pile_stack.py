"""
    Travailler avec des piles (stacks) en Python.
    Une pile est une structure de données qui suit le principe LIFO(Last In - Frist Out) qui veut dire 
    les derniers éléments ajoutés sont les premiers à être retirés.

    Les fonctionnalités de base d'une pile sont :
    - push : ajouter un élément au sommet de la pile
    - pop : retirer l'élément du sommet de la pile
    - peek : obtenir l'élément du sommet de la pile sans le retirer
    - is_empty : vérifier si la pile est vide
    - size : obtenir le nombre d'éléments dans la pile
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        """Ajouter un élément au sommet de la pile."""
        new_node = Node(data) #class nOde a été defini dans le fichier liste_chainee.py
        if self.top:
            new_node.next =self.top
        self.top = new_node

        # augmenter la taille de la pile
        self.size +=1

    # methode pop pour retirer l'élément du sommet de la pile

    def pop(self):
        if self.top is None:      # si la pile est vide retourne None
            return None
        else:                       # si la pile n'est pas vide, retire l'élément du sommet
            popped_node = self.top
            self.top = self.top.next
            self.size -= 1
            return popped_node.data
""""
Utilisation de LifoQueue de python 

"""
import queue
from queue import LifoQueue, SimpleQueue

# create a stack infinite size
my_book_stack = queue.LifoQueue(maxsize=0)  

# add an element to the stack
my_book_stack.put("Python for Data Analysis")
my_book_stack.put("Automate the Boring Stuff with Python")

# remove an element from the stack
print(my_book_stack.get())  # Output: Automate the Boring Stuff with Python


"""
Travailler avec les files d'attente (queues) en Python.
Une file d'attente est une structure de données qui se base sur le principe FIFO(First In First Out)
Les fonctionnalités de base d'une file d'attente sont :
- enqueue : ajouter un élément à la fin de la file d'attente
- dequeue : retirer l'élément du début de la file d'attente
- peek : obtenir l'élément du début de la file d'attente sans le retirer
- is_empty : vérifier si la file d'attente est vide
- size : obtenir le nombre d'éléments dans la file d'attente
- Avec la librairie queue de Python, on peut utiliser la classe Queue pour implémenter une file d'attente.
"""

class PrinterTasks:
    def __init__(self):
        self.queue = queue.Queue()

    def add_task(self, task):
        """Ajouter une tâche à la file d'attente."""
        self.queue.enqueue(task)
    
    def has_elements(self):
        return self.head != None

    def print_task(self):

        while self.queue.has_elements():
            task = self.queue.dequeue()
            print(f"Impression de la tâche : {task}")
            self.queue.task_done()


## my orders queue
my_orders_queue = queue.SimpleQueue()
my_orders_queue.enqueue("Order 1")
my_orders_queue.enqueue("Order 2")
my_orders_queue.enqueue("Order 3")