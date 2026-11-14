while True:
    print("1.add")
    print("2.subtract")
    print("3.quit")
    choice=input("choose: ")
    if choice=="1":
        a=int(input("first number:"))
        b=int(input("second number:"))
        print("result:",a+b)
    elif choice=="2":
        a=int(input("first number:"))
        b=int(input("second number:"))
        print("result:",a-b)
    elif choice=="3":
        break
    else:
        print("invalid choice.")