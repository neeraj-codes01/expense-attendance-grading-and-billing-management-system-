age=int(input("enter age:"))
gpa=float(input("enter gpa:"))
income=int(input("enter family income:"))
eligibility=(age >=18)and (gpa >=3.0) and (income<100000)
if eligibility:
    print("eligibility for scholarship")
else:
    print("not eligible for scholarship")