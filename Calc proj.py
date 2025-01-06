def calculator():
    print("Calculator project")
    print("Operators: +, -, *, /")
    
    n1 = float(input("Enter first number: "))
    op = input("Enter operator: ")
    n2 = float(input("Enter second number: "))

    if op == '+':
        print("Result:", n1 + n2)
    elif op == '-':
        print("Result:", n1 - n2)
    elif op == '*':
        print("Result:", n1 * n2)
    elif op == '/':
        if n2 != 0:
            print("Result:", n1 / n2)
        else:
            print("Error: Division by zero!")
    else:
        print("Invalid op!")

calculator()