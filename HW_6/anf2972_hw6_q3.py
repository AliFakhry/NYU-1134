from DoublyLinkedList import *

class CompactString:

    def __init__(self, orig_str):
        self.data = DoublyLinkedList()
        self.size = 0
        if orig_str != "":
            for iter in range(len(orig_str)):
                if self.data.is_empty():
                    self.data.add_first((orig_str[iter], 1))
                else:
                    if self.data.trailer.prev.data[0] == orig_str[iter]:
                        val = self.data.trailer.prev.data[1]
                        self.data.trailer.prev.data = (orig_str[iter], val+1)
                    else:
                        self.data.add_last((orig_str[iter], 1))
                self.size += 1

    def __add__(self, other):

        update_str = CompactString("")
        starting_index = self.data.header.next
        other_index = other.data.header.next

        for i in range(len(self.data)):
            if starting_index.next.data == None:
                break
            else:
                update_str.data.add_last(starting_index.data)
                starting_index = starting_index.next

        if starting_index.data[0] == other.data.header.next.data[0]:
            new_tup = (starting_index.data[0], starting_index.data[1] + other.data.header.next.data[1])
            update_str.data.add_last(new_tup)
            other_index = other.data.header.next.next
        else:
            update_str.data.add_last(starting_index.data)
            other_index = other.data.header.next

        for i in range(len(other.data)):
            if other_index.data == None:
                break
            else:
                update_str.data.add_last(other_index.data)
                other_index = other_index.next

        return update_str

    def __lt__(self, other):

        self_head = self.data.header.next
        other_head = other.data.header.next

        while self_head.data == other_head.data:

            if self_head == None:
                break

            else:
                self_head = self_head.next
                other_head = other_head.next

        if (self_head.data is None and other_head.data is None) or (self_head.data is not None and other_head.data is None):
            return False

        elif self_head.data is None and other_head.data is not None:
            return True

        else:
            if self_head.data[0] == other_head.data[0]:

                if self_head.data[1] > other_head.data[1]:

                    if other_head.next.data == None:
                        return False

                    if (self_head.data[0] < other_head.next.data[0]) == True:
                        return True

                    else:
                        return False

                else:

                    if self_head.next.data is None or (self_head.next.data[0] < other_head.data[0]):
                        return True

                    else:
                        return False

            else:
                if self_head.data[0] < other_head.data[0] == True:

                    return True
                else:

                    return False

    def __le__(self, other):

        self_head = self.data.header.next
        other_head = other.data.header.next

        while self_head.data == other_head.data:

            if self_head == None:
                break

            else:
                self_head = self_head.next
                other_head = other_head.next

        if (self_head.data is None and other_head.data is None) or (
                self_head.data is not None and other_head.data is None):
            return False

        elif self_head.data is None and other_head.data is not None:
            return True

        else:
            if self_head.data[0] == other_head.data[0]:

                if self_head.data[1] > other_head.data[1]:

                    if other_head.next.data == None:
                        return True

                    if (self_head.data[0] < other_head.next.data[0]) == True:
                        return True

                    else:
                        return False

                else:

                    if self_head.next.data is None:

                        return True

                    if (self_head.next.data[0] < other_head.data[0]) == True:

                        return True
                    else:

                        return False

            else:
                if self_head.data[0] < other_head.data[0] == True:

                    return True
                else:

                    return False

    def __gt__(self, other):
        return not(self <= other)

    def __ge__(self, other):
        return not(self < other)

    def __repr__(self):
        range = self.data.header.next
        total_submit = ""
        while range.data is not None:
            new_val = range.data[1] * range.data[0]
            total_submit += new_val
            range = range.next

        return total_submit
#
# s1 = CompactString("aaaaabbbaaac")
# s2 = CompactString("aaaaaaacccaaaa")
# s3 = s2 + s1
# print(s1 >= s2)
# print(s2 >= s1)