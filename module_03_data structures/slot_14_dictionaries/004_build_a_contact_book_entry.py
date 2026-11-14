contact={}
contact["name"]=input("enter your name:")
contact["phone"]=input("enter phone number:")
contact["email"]=input("enter email address:")
print("contact saved:")
for key,value in contact.items():
    print(key,":",value)