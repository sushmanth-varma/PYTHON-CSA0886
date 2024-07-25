# Input: number from user
number = int(input("Enter a number: "))

# Loop to print the pattern
for i in range(1, number + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # Newline after each row
