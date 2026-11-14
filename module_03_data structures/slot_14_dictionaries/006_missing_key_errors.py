# bug accessing a key that doesn't exist
person={"name":"bob"}
#print(person["age"])#keyError:"age"
# fix1: check first with 'in'
if "age" in person:
    print(person["age"])
else:
    print("age not set")
# fix2: use.get() with a default value(no error,ever)
print(person.get("age","not set"))# prints:not set