def split_parity(lst):
    pointer = 0
    count = True
    for i in range(len(lst)):

            if (lst[i] % 2 !=0):
                if (count ==True):
                    temp = lst[i]
                    lst[i] = lst[0]
                    lst[0] = temp
                    count = False
                else:
                    temp = lst[i]
                    lst[i] = lst[pointer+1]
                    lst[pointer + 1] = temp
                    pointer += 1

    return lst


