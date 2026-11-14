# rewrite this fragile list-of-tuples record using a list of dictionaries instead student_old=[("alice",22,"cse"),("bob",21,"it")]
students_old=[("alice",22,"cse"),("bob",21,"it")]
students_new=[
    {"name":"alice","age":22,"branch":"cse"},
    {"name":"bob","age":21,"branch":"it"},
]
for s in students_new:
    print(s["name"],"is",s["age"],"in",s["branch"])
