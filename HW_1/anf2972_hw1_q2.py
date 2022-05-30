def shift(lst, k, shift = "left"):

    if shift == "left":
      for i in range(0, k):
        original_value = lst[0]
        for j in range(len(lst)):
            if j + 1 == len(lst):
                lst[j] = original_value
            else:
                temp_val = lst[j+1]
                lst[j] = temp_val

    elif shift == "right":
        for i in range(0, k):
            original_value = lst[len(lst)-1]
            for j in range(len(lst)-1, -1, -1):
                if j == 0:
                    lst[j] = original_value
                else:
                    temp_val = lst[j - 1]
                    lst[j] = temp_val
