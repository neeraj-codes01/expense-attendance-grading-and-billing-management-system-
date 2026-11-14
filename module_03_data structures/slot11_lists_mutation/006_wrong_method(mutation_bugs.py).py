'''students=["alice","bob"]
students.remove("charlie") # valueError charlie is not in the list
students=students.append("dave") # wrong: students become none!
print(students)''' #none

students=["alice","bob"]
if "charlie" in students:
    students.remove("charlie")
students.append("dave")# bug is fixed: call append() without reassigning
print(students)
