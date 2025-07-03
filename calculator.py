def calculator():
     while True:
          print("\n Simple Calculator!!")
          print("1.Addition")
          print("2.Subtraction")
          print("3.Multiplication")
          print("4.Division")
          print("5.Exit")
          choice = input("Enter your choice from 1 to 5:")
          if choice == '5':
               print("Exiting!!")
               break
          if choice not in ['1','2','3','4']:
               print("Invalid choice.Please select a valid option.")
               continue
          try:
               num1 = float(input("Enter first number:"))
               num2 = float(input("Enter the second number:"))
          except ValueError:
               print("Invalid input.please enter numeric values.")
               continue
          if choice == '1':
               result = num1 + num2
               operator = '+'
               print(f"Result : {num1} {operator} {num2} = {result} ")
          elif choice == '2':
               result = num1 - num2
               operator = '-'
               print(f"Result : {num1} {operator} {num2} = {result}")
          elif choice == '3':
               result = num1 * num2
               operator = '*'
               print(f"Result : {num1} {operator} {num2} = {result}")
          elif choice == '4':
               if num2 == 0:
                    print("Error: cannot divide by zero.")
                    continue
               result = num1 / num2
               operator = '/'
               print(f"Result : {num1} {operator} {num2} = {result}")
calculator()