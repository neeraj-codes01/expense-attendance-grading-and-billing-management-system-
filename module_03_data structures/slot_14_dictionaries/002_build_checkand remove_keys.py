person={}
person["name"]="bob"
person["age"]=22
print(person)

if "city" in person:
    print(person["city"])
else:
    print("city not found")
del person ["age"]
print(person)