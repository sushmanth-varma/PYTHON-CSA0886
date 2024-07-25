# Input student details
name = input("Enter the student's name: ")
reg_no = input("Enter the student's register number: ")

# Input marks for 5 subjects
marks = []
for i in range(1, 6):
    marks.append(float(input(f"enter the marks:{i}")))          
# Calculate total marks
total_marks = sum(marks)
# Display student details
print("\nStudent Mark Sheet:")
print(f"Name: {name}")
print(f"Register Number: {reg_no}")
print(f"Marks: {marks}")
print(f"Total Marks: {total_marks}")
