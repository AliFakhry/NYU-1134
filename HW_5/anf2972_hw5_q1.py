from ArrayStack import *

def solution_values(user_input, dict_1):
    stack = ArrayStack()

    for i in range(len(user_input)):
        if user_input[i] in dict_1:
            stack.push(dict_1[user_input[i]])
        if user_input[i].isdigit():
            stack.push(user_input[i])
        elif user_input[i] == "+":
            val1 = stack.pop()
            val2 = stack.pop()
            stack.push(int(val2) + int(val1))
        elif user_input[i] == "/":
            val1 = stack.pop()
            val2 = stack.pop()
            stack.push(int(val2) / int(val1))
        elif user_input[i] == "*":
            val1 = stack.pop()
            val2 = stack.pop()
            stack.push(int(val2) * int(val1))
        elif user_input[i] == "-":
            val1 = stack.pop()
            val2 = stack.pop()
            stack.push(int(val2) - int(val1))

    val = stack.pop()
    return val

def postfix_step_one():
    new_dict = {}
    input_val = input("--> ")
    while (input_val != "done()"):
        input_val = input_val.strip()
        new_val = input_val.split(" ")
        new_lst = []
        for iter in new_val:
            iter.replace(' ', "")
            new_lst.append(iter)

        if len(new_lst) > 2 and new_lst[1] == "=":
            calculate_val = solution_values(new_lst[2:], new_dict)
            new_dict[new_lst[0]] = calculate_val
            print(new_lst[0])
        else:
            print(solution_values(new_lst, new_dict))

        input_val = input("--> ")

postfix_step_one()
