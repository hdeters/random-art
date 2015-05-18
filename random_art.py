import random
import math

# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.

class Gen_expression:
    def __init__(self):
        self.func_list = self.generate_list()

    def generate_list(self):
        functions = ["sin", "cos", "avg", "pow"]
        func_list = []
        for i in range(random.randint(2,20)):
            func_list.append(random.choice(functions))
            i -= 1
        return func_list

    def __str__(self):
        string = ""
        count = 0
        for func in self.func_list:
            if func == "sin":
                string = string + "Sin(Pi * Sin(x * "
            elif func == "cos":
                string = string + "Cos(Cos(y * "
            elif func == "avg":
                string = string + "avg("
            elif func == "pow":
                string = string + "(x^2 - y^2 "
            count += 1

        string = string + "(x + y)/2"

        for i in range(count):
            string = string + ")"

        return string

    def __repr__(self):
        string = ""
        count = 0
        for func in self.func_list:
            if func == "sin":
                string = string + "Sin(Pi * Sin(x * "
            elif func == "cos":
                string = string + "Cos(Cos(y * "
            elif func == "avg":
                string = string + "avg("
            elif func == "pow":
                string = string + "(x^2 - y^2 "
            count += 1

        string = string + "(x + y)/2"

        for i in range(count):
            string = string + ")"

        return string

def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    funcs = Gen_expression()
    return (funcs)

def run_expression(funcs, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    val = evaluate_funcs(funcs.func_list, x, y, (x + y)/2, len(funcs.func_list)-1)
    return val

def evaluate_funcs(funcs, x, y, current_val = 1, idx = 1):
    func_list = funcs
    value = current_val
    if idx != 0:
        if func_list[idx] == "sin":
            new_value = math.sin(math.pi * math.sin(x * value))
        elif func_list[idx] == "cos":
            new_value = math.cos(math.cos(value * y))
        elif func_list[idx] == "avg":
            new_value = (value * math.pi) + (value * math.e)/2
        elif func_list[idx] == "pow":
            new_value = x**2 - y**2
        idx -= 1
        return evaluate_funcs(func_list, x, y, new_value, idx)
    else:
        return value
