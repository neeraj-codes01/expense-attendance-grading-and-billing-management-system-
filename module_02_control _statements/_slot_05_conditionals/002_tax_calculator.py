monthly_salary=int(input("enter monthly salary:"))
annual_salary=monthly_salary*12
print("annual salary:",annual_salary)
if annual_salary>130000:  # we are not use commas in numbers
    print("you are eligible for tax")
else:
    print("you are not eligible for tax")