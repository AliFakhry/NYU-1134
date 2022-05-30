from ArrayStack import *

class MaxStack:

    def __init__(self):
        self.data = ArrayStack()
        self.maximum = None

    def is_empty(self):
        if len(self) == 0:
            return True
        else:
            return False

    def __len__(self):
        return len(self.data)

    def push(self, e):
        tup = (e, self.maximum)
        self.data.push(tup)
        if self.maximum is None:
            self.maximum = e
        elif e > self.maximum:
            self.maximum = e

    def top(self):
        if self.is_empty():
            raise Exception ("Stack Empty")
        else:
            return self.data.top()[0]

    def pop(self):

        if self.is_empty():
            raise Exception ("Stack Empty")
        else:
            temp_top = self.data.pop()
            if temp_top[1] is None:
                self.maximum = temp_top[1]
                return temp_top[0]
            elif temp_top[0] > temp_top[1]:
                self.maximum = temp_top[1]
                return temp_top[0]
            else:
                return temp_top[0]

    def max(self):
        if not self.is_empty():
            return self.maximum
        else:
            raise Exception("Stack Empty")

