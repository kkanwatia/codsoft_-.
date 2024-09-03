def ask(num1 = None):
    if num1 is None:    
        num1 = float(input("Enter a number: "))
    operation = input("Enter the operation(+,-,*,/): ")
    num2 = float(input("Enter next number: "))
    calculate(num1 ,operation, num2)

def calculate(num1 ,operation, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    print(f"{num1} {operation} {num2} = {result}")
    again(result)

def again(result):
    user = input("Do you want to continue? y/n: ")
    if user == "y":
        user2 = input("Do you want to continue with previous result as first number? y/n: ")
        if user2 == "y":
            ask(result)
        else:
            ask()
    else:
        print("\nThank you for using the program.")

print("___________Welcome to calculator program___________\n".upper())
ask()

