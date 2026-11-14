#broken: this single function mixes validation,calculation,and output--
#hard to test,hard to reuse,hard to debug
def handle_student(name,marks):
    if marks<0 or marks>100:
        print("invalid marks")
        return

    if marks>=60:
        grade="pass"
    else:
        grade="fail"
    print(f"{name}: {grade}")
#fixed: split into three focused functions
def is_valid_marks(marks):
    return 0<=marks <=100
def get_pass_fail(marks):
    return "pass" if marks>=60 else "fail"

def print_student_result(name,result):
    print(f"{name}:{result}")
