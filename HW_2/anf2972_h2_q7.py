def findChange(lst01):
    upper_bound = len(lst01) - 1
    lower_bound = 0
    center_bound = (lower_bound + upper_bound)//2

    while lower_bound < upper_bound:
        if lst01[center_bound] == 1 and lst01[center_bound-1] ==0:
            return center_bound

        elif lst01[center_bound] == 0:
            lower_bound = center_bound + 1
            center_bound = (center_bound + upper_bound) // 2

        elif lst01[upper_bound] == 1:
            upper_bound = center_bound - 1
            center_bound = (center_bound + upper_bound) // 2



