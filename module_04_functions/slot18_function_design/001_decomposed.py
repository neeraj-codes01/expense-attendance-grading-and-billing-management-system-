def get_marks():
    marks=-1
    while marks<0 or marks>100:
        marks=int(input("enter marks(0-100):"))
        if marks<0 or marks>100:
            print("invalid.try again.")
    return marks


def calculate_grade(marks):
    if marks>=90:
        return "a"
    elif marks>=75:
        return "b"
    elif marks>=60:
        return "c"
    else:
        return "f"



def print_result(name,marks,grade):
    print(f"{name}:{marks} marks-> grade {grade}")

name=input("name")
marks=get_marks()
grade=calculate_grade(marks)
print_result(name,marks,grade)