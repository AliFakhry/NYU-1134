def find_duplicates(lst):

    new_arr = [0] * len(lst)
    duplicate_arry = []

    for i in range(len(lst)):
        new_val = lst[i]
        new_arr[new_val] += 1

    for j in range(len(new_arr)):
        if new_arr[j] > 1:
            duplicate_arry.append(j)

    return duplicate_arry
