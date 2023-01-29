print("Basic calculator")


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def multi(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


operators = {
    "+": add,
    "-": sub,
    "*": multi,
    "/": div
}

first_number = int(input("Enter first number: "))

for operator in operators:
    print(operator)
option = input("Pick a operation from above: ")
second_number = int(input("Enter second number: "))

calculation_function = operators[option]

result = calculation_function(first_number, second_number)

print(result)
