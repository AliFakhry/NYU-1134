n = 5

def sum_squares(n):
    total_sum = 0
    for i in range(n):
        if i > 0:
            total_sum += (i**2)
    return total_sum

print(sum([i**2 for i in range(1,n)]))

def odd_squares(n):
    total_sum = 0
    for i in range(n):
        if i % 2 == 1 and i > 0:
            total_sum += (i**2)
    return total_sum

print(sum([j**2 for j in range(1,n) if j % 2 == 1 and j > 0]))