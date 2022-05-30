from DoublyLinkedList import *

class LinkedQueue:
    def __init__(self):
        self.data = DoublyLinkedList()
        self.size = self.data.size

    def __len__(self):
        return(self.size)

    def is_empty(self):
        if len(self) == 0:
            return True
        else:
            return False

    def enqueue(self, val):

        self.data.add_last(val)
        self.size += 1

    def dequeue(self):
        if self.is_empty() == True:
            raise Exception("Queue is empty")
        else:
            val = self.data.delete_first()
            return val

    def first (self):
        if self.is_empty() == True:
            raise Exception("Queue is empty")
        else:
            return self.data.header.next.data