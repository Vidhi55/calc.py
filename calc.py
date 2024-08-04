def calculator():
    
    print("Select operation:")
    print("1. Subtraction")
    print("2. Addition")
    print("3. Multiplication")
    print("4. Division")
    
    operation_choice = input("Enter operation_choice (1/2/3/4): ")
    
    if operation_choice in ['1', '2', '3', '4']:
       
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if operation_choice == '1':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation_choice == '2':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation_choice == '3':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation_choice == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Error! Division by zero.")
    else:
        print("Invalid input. Please enter a number between 1 and 4.")
    
calculator()
