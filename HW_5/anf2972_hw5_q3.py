from ArrayStack import ArrayStack
from ArrayDeque import ArrayDeque

class MidStack:
    def __init__(self):
        self.under_stack = ArrayStack()
        self.upper_stack = ArrayDeque()

    def __len__(self):
        len_bottom = len(self.under_stack)
        len_top = len(self.upper_stack)
        return len_bottom + len_top

    def is_empty(self):
        if len(self) == 0:
            return True
        else:
            return False

    def push(self, e):
        if len(self) % 2 == 0:
            self.upper_stack.enqueue_first(e)
        elif len(self) % 2 == 1:
            self.under_stack.push(self.upper_stack.last())
            self.upper_stack.dequeue_last()
            self.upper_stack.enqueue_first(e)

    def pop(self):
        if len(self) == 0:
            raise Exception ("Stack Empty")
        else:
            if len(self) % 2 == 1:
                return self.upper_stack.dequeue_first()
            elif len(self) % 2 == 0:
                self.upper_stack.enqueue_last(self.under_stack.pop())
                return self.upper_stack.dequeue_first()

    def top(self):
        if (self.is_empty()):
            raise Exception("Stack Empty")
        else:
            return self.upper_stack.first()

    def mid_push(self, e):
        if len(self) % 2 == 0:
            self.upper_stack.enqueue_last(e)
        elif len(self) % 2 == 1:
            temp = self.upper_stack.last()
            self.upper_stack.dequeue_last()
            self.upper_stack.enqueue_last(e)
            self.under_stack.push(temp)


