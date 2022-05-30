from ArrayStack import *
from ArrayQueue import *

def permutations(lst):
    stack = ArrayStack()
    queue = ArrayQueue()
    final = []

    for z in range(len(lst)):
        stack.push(lst[z])

    queue.enqueue(list(str(stack.pop())))
    val = (queue.dequeue())
    val[0] = int(val[0])
    queue.enqueue(val)

    while len(stack) > 0:
        new_elem = stack.pop()
        for i in range(len(queue)):
            first_val = queue.first()
            possible_index = len(first_val)+1
            for index in range(possible_index):
                first_updated = first_val[:]
                first_updated.insert(index, new_elem)
                queue.enqueue(first_updated)
            queue.dequeue()

    for i in range(len(queue)):
        final.append(queue.dequeue())
    return final
