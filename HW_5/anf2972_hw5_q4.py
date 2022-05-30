from ArrayStack import *

class Queue:

    def __init__(self):
        self.remove_stack = ArrayStack()
        self.value_stack = ArrayStack()
        self.front = None

    def __len__(self):
        return len(self.value_stack)

    def is_empty(self):
        if len(self.value_stack) == 0:
            return True
        else:
            return False

    def enqueue(self, e):
        if self.is_empty() == True:
            self.front = e
            self.value_stack.push(e)
        else:
            self.value_stack.push(e)

    def first(self):
        if self.is_empty() == True:
            raise Exception ("Empty Queue.")
        else:
            return self.front

    def dequeue(self):
        for val in range(len(self.value_stack)):
            new_val = self.value_stack.pop()
            self.remove_stack.push(new_val)
        top_val = self.remove_stack.pop()
        if not self.remove_stack.is_empty():
            self.front = self.remove_stack.top()
        else:
            self.front = None
        for iter in range(len(self.remove_stack)):
            self.value_stack.push(self.remove_stack.pop())
        return top_val