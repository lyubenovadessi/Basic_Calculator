import calc_logo

def add(num1, num2):
    return num1 + num2

def subtract(num1,  num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    print(calc_logo.logo)
    should_accumulate = True
    first_number_input  = float(input("Enter first number: \n"))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_input = input("Pick an operation: \n")
        second_number_input = float(input("Enter second number: \n"))
        result = operations[operation_input](first_number_input, second_number_input)
        print(f"{first_number_input} {operation_input} {second_number_input} = {result}")

        choice = input(f"Continue calculating with {result}? (y/n): \n")
        if choice == "y":
            first_number_input = result
        else:
            should_accumulate = False
            print("\n*20")
            calculator()

calculator()



