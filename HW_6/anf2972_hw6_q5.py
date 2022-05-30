from DoublyLinkedList import *

def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    def merge_helper(srt_lnk_lst1, srt_lnk_lst2, curr_1, curr_2, merge_values):

        if curr_1 == srt_lnk_lst1.trailer and curr_2 == srt_lnk_lst2.trailer:
            return

        elif curr_1 == srt_lnk_lst1.trailer or curr_2 == srt_lnk_lst2.trailer:
            if curr_1 == srt_lnk_lst1.trailer:
                merge_values.add_last(curr_2.data)
                curr_2 = curr_2.next

            elif curr_2 == srt_lnk_lst1.trailer:
                merge_values.add_last(curr_1.data)
                curr_1 = curr_1.next

            merge_helper(srt_lnk_lst1, srt_lnk_lst2, curr_1, curr_2, merge_values)

        else:
            if curr_2.data > curr_1.data:
                merge_values.add_last(curr_1.data)
                curr_1 = curr_1.next

            elif curr_1.data > curr_2.data:
                merge_values.add_last(curr_2.data)
                curr_2 = curr_2.next

            else:
                data = curr_1.data
                curr_1 = curr_1.next
                curr_2 = curr_2.next

                merge_values.add_last(data)
                merge_values.add_last(data)

            merge_helper(srt_lnk_lst1, srt_lnk_lst2, curr_1, curr_2, merge_values)

    if srt_lnk_lst1.is_empty() or srt_lnk_lst2.is_empty():
        if srt_lnk_lst1.is_empty():
            return srt_lnk_lst2
        else:
            return srt_lnk_lst1
    else:
        curr_1 = srt_lnk_lst1.header.next
        curr_2 = srt_lnk_lst2.header.next
        merge_values = DoublyLinkedList()
        merge_helper(srt_lnk_lst1, srt_lnk_lst2, curr_1, curr_2, merge_values)
        return merge_values


# srt_lnk_lst1 = DoublyLinkedList()
#
# srt_lnk_lst1.add_last(1)
# srt_lnk_lst1.add_last(3)
# srt_lnk_lst1.add_last(5)
# srt_lnk_lst1.add_last(6)
# srt_lnk_lst1.add_last(8)
#
# srt_lnk_lst2 = DoublyLinkedList()
#
# srt_lnk_lst2.add_last(2)
# srt_lnk_lst2.add_last(3)
# srt_lnk_lst2.add_last(5)
# srt_lnk_lst2.add_last(10)
# srt_lnk_lst2.add_last(15)
# srt_lnk_lst2.add_last(18)
#
# print(merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2))