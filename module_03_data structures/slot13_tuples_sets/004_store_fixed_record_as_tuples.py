# store 3 students(name,age,city)tuple in a list,then unpack each
students=[
    ("neeraj",22,"rewari"),
    ("bob",21,"delhi"),
    ("pankaj",23,"jaipur"),
]
for student in students:
    name,age,city=student
    print(f"{name} is {age} years old and lives in {city}")

