string = input("Enter a string to convert to a number: ")

try:

    number = int(string)
    print(f"The string '{string}' has been successfully converted to the number {number}.")
except ValueError:
    
    print(f"The string '{string}' is not a valid number.")
