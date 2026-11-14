marks=int(input("enter your marks:"))
if marks>=90:
    grade="a"
elif marks>=80:
    grade="B"
elif marks>=60:
    grade="c"
else:
    grade="fail"
print("grade:",grade)
