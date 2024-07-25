# Input student details
name = input("Enter the student's name: ")
reg_no = input("Enter the student's register number: ")

# Input marks for 5 subjects
marks = []
for i in range(1, 6):
    while True:
        try:
            mark = float(input(f"Enter mark for subject {i}: "))
            if mark < 0 or mark > 100:
                print("Please enter a valid mark between 0 and 100.")
            else:
                marks.append(mark)
                break
        except ValueError:
            print("Please enter a valid number.")

# Calculate total marks
total_marks = sum(marks)

# Display student details
print("\nStudent Mark Sheet:")
print(f"Name: {name}")
print(f"Register Number: {reg_no}")
print(f"Marks: {marks}")
print(f"Total Marks: {total_marks}")
