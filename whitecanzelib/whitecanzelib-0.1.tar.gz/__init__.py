def add_numbers(num1, num2):
    return num1+num2


def subtract_numbers(num1, num2):
    return num1-num2


def multiply_numbers(num1, num2):
    return num1*num2


def divide_numbers(num1, num2):
    return num1/num2


def power_numbers(num, power):
    return num ** power
    
def total_numbers(*args):
    x = 0
    for i in range(len(args)):
        x+=args[i]
    return x

print(total_numbers(9,5,4,1,1,5,5))