age=-1
while age<0 or age>120:
    age=int(input("enter age(0-120):"))
    if age<0 or age>120:
        print("invalid.try again.")
print("valid age recorded:",age)