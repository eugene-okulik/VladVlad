num1 = int((input("Enter first number: ")))
num2 = int((input("Enter second number: ")))


def oper(func):
    def wrapper(first, second, operation=None):
        if first < 0 or second < 0:
            operation = '*'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'
        return func(first, second, operation)
    return wrapper


@oper
def calc(first, second, operation):
    if operation == '*':
        return first * second
    elif operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second


result = calc(num1, num2)
print(result)
