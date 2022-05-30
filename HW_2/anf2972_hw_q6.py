def two_sum(srt_lst, target):
    left_pointer = 0
    right_pointer = len(srt_lst) -1

    while srt_lst[left_pointer] + srt_lst[right_pointer] != target:

        total = srt_lst[left_pointer] + srt_lst[right_pointer]

        if left_pointer == right_pointer:
            return None

        elif total > target:
            right_pointer -= 1

        elif total < target:
            left_pointer += 1


    return (left_pointer, right_pointer)
