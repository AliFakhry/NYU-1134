def remove_all(lst, value):
    total_count = 0
    length_lst = len(lst)
    for i in range(length_lst):
        if lst[i] != value:
            temp = lst[i]
            lst[i-total_count] = temp
        elif lst[i] == value:
            total_count += 1
    for j in range(total_count):
        lst.pop()

    return lst
