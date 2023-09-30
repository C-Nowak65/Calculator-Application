def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator():

    num1 = float(input("What is the first number? "))
    print("What operation would you like to complete? ")
    for key in operation:
        print(key)

    should_continue = True

    while should_continue:

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))

        calculation_function = operation[operation_symbol]
        answer = calculation_function(n1=num1, n2=num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calcualtinng with {answer} or type 'n' to start a new operation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            functions.calculator()