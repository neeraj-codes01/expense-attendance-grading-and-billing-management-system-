# A user gets a loan only if they are employed and have a credit card above 700
is_employed=input("are you employed? (yes/no):")=="yes"
credit_score=int(input("enter your credit score:"))
if is_employed and credit_score>700:
    print("loan approved")
else:
    print("loan not approved")