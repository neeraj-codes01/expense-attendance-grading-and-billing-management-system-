students=[]
students.append("alice")
students.append("bob")
print(students)# append means add an item in the last
students.insert(1,"neeraj")
print(students)


students.remove("alice")
print(students)
for student in students:#traverse
    print(student)