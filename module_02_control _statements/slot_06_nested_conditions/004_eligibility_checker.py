# build an eligibility checker for a job:
# criteria : age>=21, has a degree (true/false), experience>=2years
age=int(input("enter age:"))
has_degree=input("do you have a degree(yes/no):")=="yes"
experience=int(input("year of experience:"))
if age>=21:
    if has_degree:
        if experience>=2:
            print("you are eligible for the job")
        else:
            print("you need at least two years of experience")
    else:
        print("you must have a degree.")
else:
    print("you must be at least 21 years old.")
        