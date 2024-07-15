# Define the lists of students
allowed_students = ["Alice", "Bob", "Charlie", "David", "Eve"]
denied_students = ["Oliver", "Patricia", "Quinn", "Rachel", "Sam"]

# Define a function to check if a student is allowed to write the exam
def can_write_exam(student):
  if student in allowed_students:
    return True
  elif student in denied_students:
    return False
  else:
    return "Student not found"

# Test the function
students = ["Alice", "Oliver", "Bob", "Quinn", "Eve", "Sam", "John"]
for student in students:
  result = can_write_exam(student)
  print(f"{student} can write the exam: {result}")