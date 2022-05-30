def permutations(lst, low, high):
    if len(lst) == 0:
        return [[]]
    elif (low == high):
        return [[lst[low]]]
    updated_list = []
    range_val = (high - low + 1)
    for i in range(range_val):
        val = permutations(lst,low+1,high)
        for sublst in val:
            low_val = lst[low]
            sublst.insert(i, low_val)
            updated_list.append(sublst)
    return updated_list