# Initialize the sum to 0
total_sum = 0

# Infinite loop to take input until a negative number is entered
while True:
    # Input: number from user
    number = int(input("Enter a number (negative number to stop): "))
    
    # Check if the number is negative
    if number < 0:
        break
    
    # Check if the number is positive and add it to the total sum
    if number > 0:
        total_sum += number

# Output: display the total sum
print(f"Sum of all positive numbers entered: {total_sum}")
