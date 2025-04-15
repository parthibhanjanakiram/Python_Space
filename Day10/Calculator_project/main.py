
import calc_functions

num1 = float(input("What is the first number?: "))

# print(" + \n - \n * \n / \n ")

flag = True

while(flag):
    print(" + \n - \n * \n / \n ")
    operation_input = input("Pick an operation : ")
    num2 = float(input("What is the next number?: "))

    if operation_input == "+":
        num1 = calc_functions.addition(num1, num2)
    elif operation_input == '-': 
        num1 = calc_functions.subtraction(num1, num2)
    elif operation_input == '*':
        num1 = calc_functions.multiplication(num1, num2)   
    elif operation_input == '/':
        num1 = calc_functions.division(num1, num2)
    else:
        print("Please try again...")
    
    continue_calculation = input(f"Type 'Y' to continue calculating with {num1}, or Type 'N' to start new calculation: ").lower()
    if continue_calculation == 'n':
        flag = False
    else:
        None
