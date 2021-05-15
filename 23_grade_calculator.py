marks = int(input("Enter the marks of the student: "))
if marks >= 90:
    print("Student's grade: A")
elif 90 > marks >= 75:
    print("Student's grade: B")
elif 75 > marks >= 60:
    print("Student's grade: C")
else:
    print("Student's grade: D")
