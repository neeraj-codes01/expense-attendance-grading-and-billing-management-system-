while True:
    age=input("enter age:")
    if age.lower()=="stop":
        print("program completed")
        break
    customer_age=int(age)
    if customer_age<=5:
        price="free"
    elif customer_age>=5 and customer_age<=12:
        price=100
    elif customer_age>=13 and customer_age<=59:
        price=200
    else:
        price=120
    print("applicable ticket price:",price)
print("program completed")