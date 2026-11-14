#given " Rahul,22,Delhi,split,into name,age,city,and print each
record="Rahul,22,delhi"
parts=record.split(",")
name=parts[0]
age=parts[1]
city=parts[2]
print(f"name: {name},age:{age},city:{city}")