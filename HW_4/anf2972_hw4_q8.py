def flat_list(nested_lst, low, high):
    return_val = []
    if isinstance(nested_lst[low], list):
        return_val = flat_list(nested_lst[low], 0, len(nested_lst[low])-1)
    else:
        return_val = [nested_lst[low]]
    if low < high:
        return return_val + flat_list(nested_lst, low + 1, high)
    else:
        return return_val
