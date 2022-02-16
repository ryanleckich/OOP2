import studentclass as sc

studentID = input("Student ID: ")
DOB = input("Date of Birth: ")
DOB = int(DOB.split("/")[2])

name = input("Name: ")
classification = input(" classification - 'Sr','Jr','S' or 'F'): ")

my_student = sc.student(studentID, name, DOB, classification)

my_student.set_age(DOB)
my_student.set_reg_time(classification)

print("Student Age: ", my_student.get_age())
print("Student Registration Date: ", my_student.get_reg_time())
