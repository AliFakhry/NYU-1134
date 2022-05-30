from DoublyLinkedList import *

class Integer:

    def __init__(self, num_str=None):
        self.data = DoublyLinkedList()
        if num_str != None:
            for i in num_str:
                self.data.add_last(int(i))

    def __add__(self, other):

        # print(self.data)
        # print(other.data)

        update_int = Integer()

        iterations = 0
        prior = 0

        larger_val = max(len(other.data), len(self.data))

        if len(self.data) <= len(other.data):
            fewer_node = self.data.trailer.prev
            higher_node = other.data.trailer.prev
            iterations = len(self.data)

        else:
            iterations = len(other.data)
            fewer_node = other.data.trailer.prev
            higher_node = self.data.trailer.prev

        difference = larger_val - iterations

        for val in range(iterations):
            new_val = fewer_node.data + higher_node.data + prior
            if new_val < 10:
                update_int.data.add_first(new_val)
                prior = 0
            else:
                update_int.data.add_first(new_val % 10)
                prior = 1

            fewer_node = fewer_node.prev
            higher_node = higher_node.prev

        if (difference > 0):
            new_iter = 0
            while new_iter < (difference):
                add_val = 0
                if higher_node.data != None:
                    add_val = higher_node.data
                new_val = prior + add_val
                if new_val < 10:
                    update_int.data.add_first(new_val)
                    prior = 0
                else:
                    update_int.data.add_first(new_val % 10)
                    prior = 1
                if prior == 1 and new_iter + 1 == difference:
                    new_iter += 0
                else:
                    new_iter += 1

                higher_node = higher_node.prev

        while update_int.data.header.next.data == 0:
            update_int.data.delete_first()

        return update_int

    def __repr__(self):
        new_str = ""
        for item in self.data:
            new_str += (str(item))
        return new_str

# n1 = Integer("007")
# n2 = Integer("20")
# print(n1 + n2)