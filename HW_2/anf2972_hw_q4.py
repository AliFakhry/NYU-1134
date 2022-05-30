def e_approx(n):
    next_iteration = 1
    total_value = 1
    for x in range(1, n+1):
        next_iteration = next_iteration / x
        total_value = total_value + next_iteration
    return total_value