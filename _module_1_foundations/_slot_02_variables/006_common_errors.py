# error 1: using a variable before defining it
print(score)  #nameError

# error 2: forgetting quotes
name=neeraj  # nameError
#fix:
name="neeraj"
# error 3: (conceptual trap): number stored as a string
age="22"
print(type(age))