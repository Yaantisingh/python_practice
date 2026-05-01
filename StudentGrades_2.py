#2 Student Grades
#Create a dictionary where the keys are student names and the values are their grades. Allow the user to:
#Add a new student and grade.
#Update an existing student’s grade.
#Print all student grades.

grades = {
    "Ashish": "A",
    "Beena": "B",
    "Kavita": "C"
}

print("Student Grades System")
print("1. Add new student")
print("2. Update student grade")
print("3. Print all grades")

choice = int(input("Enter your choice: "))

# Add new student
if choice == 1:
    name = input("Enter student name: ")
    grade = input("Enter grade: ")
    grades[name] = grade
    print("student added")
    print(grades)

# Update existing student
elif choice == 2:
    name = input("Enter student name to update:")
    if name in grades:
        grade = input("Enter new grade: ")
        grades[name] = grade
        print("Grade updated")
        print(grades)
    else:
        print("Student not found")

# Print all students
elif choice == 3:
    print("All Student Grades:")
    print(grades)

# Invalid choice
else:
    print("Invalid choice")