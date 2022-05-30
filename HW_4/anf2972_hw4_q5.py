def count_lowercase(s,low,high):
    if low == high:
        if s[low].islower():
            return 1
        else:
            return 0

    elif s[low].islower():
        return (1 + count_lowercase(s, low+1, high))
    else:
        return count_lowercase(s, low+1, high)


def is_number_of_lowercase_even(s, low, high):
    if len(s) == 1 and low == high:
        return True
    if low == high:
        if s[low].islower():
            return 1
        else:
            return 0
    elif s[low].islower():
        counter =  (1 + count_lowercase(s, low + 1, high))
    else:
        counter = count_lowercase(s, low + 1, high)

    if counter%2 == 0 or counter == 0:
        return True
    else:
        return False


