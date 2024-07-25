# Simple Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
# Take input from the user
choice= input("Enter choice (1/2/3/4): ")
if choice in ['1', '2', '3', '4']:
    if choice=='1':
        result=num1+num2
        operation='+'
    elif choice=='2':
          result=num1-num2
          operation='-'
    elif choice=='3':
          result=num1 * num2
          operation='*'
    elif choice=='4':
          result=num1/num2
          operation = '/'
    print(f"{num1} {operation} {num2} = {result}")
else:
    print("Invalid input")
