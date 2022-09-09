# Display Welcome Message and Ask User for their Name.
print("**** Welcome to the LAB grade calculator! ****")
name = input("\nWho are we calculating grades for? ==> ")

# Receive the Lab Grade and Adjust it if it is Outside the 0-100 Range.
lab_grade = int(input("\nEnter the Labs grade? ==> "))

if lab_grade > 100:
    lab_grade = 100
    print("The lab value should have been 100 or less. It has been changed to 100.")
elif lab_grade < 0:
    lab_grade = 0
    print("The lab value should have been zero or greater. It has been changed to 0")

# Receive the Exams Grade and Adjust it if it is Outside the 0-100 Range.
exams_grade = int(input("\nEnter the EXAMS grade? ==> "))

if exams_grade > 100:
    exams_grade = 100
    print("The exam value should have been 100 or less. It has been changed to 100.")
elif exams_grade < 0:
    exams_grade = 0
    print("The exam value should have been zero or greater. It has been changed to 0")

# Receive the Attendance and Adjust it if it is Outside the 0-100 Range.
attendance = int(input("\nEnter the Attendance grade? ==> "))

if attendance > 100:
    attendance = 100
    print("The attendance value should have been 100 or less. It has been changed to 100.")
elif attendance < 0:
    attendance = 0
    print("The attendance value should have been zero or greater. It has been changed to 0")

# Calculated the Weighted Grade.
weighted_grade = (lab_grade * 0.7) + (exams_grade * 0.2) + (attendance * 0.1)

# Display the Student's Grade, Rounding to the Nearest Tenth.
print(f"\nThe weighted grade for {name} is {weighted_grade:.1f}")

# See which Letter Grade the Weighted Grade will Earn the Student.
if weighted_grade >= 90:
    letter_grade = "A"
elif weighted_grade >= 80:
    letter_grade = "B"
elif weighted_grade >= 70:
    letter_grade = "C"
elif weighted_grade >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display the Student's Letter Grade and Thank the User.
print(f"{name} has a letter grade of {letter_grade}")
print("\n**** Thanks for using the Lab grade calculator ****")

