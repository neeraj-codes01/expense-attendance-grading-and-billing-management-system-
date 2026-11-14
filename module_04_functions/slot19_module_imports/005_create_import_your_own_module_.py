#in units.py:
#def validate_age(age):
 #   return 0<=age<=120
#def celsius_to_fahrenheit(c):
 #   return(c*9/5)+32
# in this file:
from utils import validate_age,celsius_to_fahrenheit
age=int(input("enter your age:"))
if validate_age(age):
    print("your age is valid")
else:
    print("your age is invalid")
temp=float(input("enter your temperature in celsius:"))
print("in fahrenheit",celsius_to_fahrenheit(temp))
