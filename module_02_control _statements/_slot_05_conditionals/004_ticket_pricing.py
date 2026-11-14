age=int(input("enter your age:"))
if age<5:
    print("free")
elif age>=5 and age<=17:
    print("Rs.150")
elif age>=18 and age<=59:
    print("RS.300")
else:
    print("Rs.100")
    print("senior discount")
