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


def calculator():

    first_number = int(input("Enter first number: "))

    for operator in operators:
        print(operator)

    should_continue = True
    while should_continue:
        option = input("Pick a operation from above: ")
        second_number = int(input("Enter second number: "))

        calculation_function = operators[option]

        result = calculation_function(first_number, second_number)

        print(f"{first_number} {option} {second_number} = {result}")

        if input(f"To continue with {result} type 'y', to start a new calculation type 'n': ") == "y":
            first_number = result
        else:
            should_continue = False
            calculator()


calculator()
