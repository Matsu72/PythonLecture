def power(base, exp):
    return base ** exp

def times(num1, num2):
    return num1 * num2

def devide(num1, num2):
    if num2 == 0:
        raise ValueError("Can not devide by zero!")
    return num1 / num2