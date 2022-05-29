import math

def factors(num):

    sqrt_num = int(math.sqrt(num))

    for i in range(1, sqrt_num + 1):
        if num % i == 0:
            yield i

    for y in range(sqrt_num -1, 0, -1):

        if num % y == 0:
            yield num // y
