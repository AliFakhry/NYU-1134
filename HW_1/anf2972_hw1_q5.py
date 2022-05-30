def fibs(n):
    lst = []
    for i in range(n):
        if i == 0 or i == 1:
            lst.append(1)
            yield lst[i]
        elif i == 2:
            lst.append(i)
            yield lst[i]
        else:
            lst.append(lst[i-1] + lst[i-2])
            yield lst[i-1] + lst[i-2]

