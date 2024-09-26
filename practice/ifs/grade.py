marks = input("insert marks:")
marksInt = int(marks)
grade = ""

if marksInt >100:
    print("Verify your marks")
    exit()


if marksInt <60:
    grade = "F"
elif marksInt <70:
    grade = "d"
elif marksInt <80:
    grade = "C"
elif marksInt <90:
    grade = "B"
elif marksInt >=90:
    grade = "A"
    
print(grade)