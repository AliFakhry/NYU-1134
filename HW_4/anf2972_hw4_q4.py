def list_min(lst,low,high):
    if len(lst) == 0:
        return lst
    elif low == high:
        return lst[low]
    else:
        val = list_min(lst, low+1,high)
        if lst[low] < val:
            val = lst[low]
        return val
