correct_password="neeraj123"
entered=""
while entered!=correct_password:
    entered=input("enter password:")
    if entered !=correct_password:
        print("password does not match. try again.")
print("access granted")