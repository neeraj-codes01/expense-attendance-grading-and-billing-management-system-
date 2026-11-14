# before: this validation logic is copy pasted 3 times
age1=int(input("enter age 1:"))
while age1<0 or age1>120:
    print("invalid age")
    age1=int(input("enter age1:"))

  #... repeated 2 more times for age2,age3...
def get_valid_age(prompt):
    age=int(input(prompt))
    while age<0 or age>120:
        print("invalid age.")
        age=int(input(prompt))
    return age
age1=get_valid_age("enter age 1:")
age2=get_valid_age("enter age 2:")
age3=get_valid_age("enter age 3:")

