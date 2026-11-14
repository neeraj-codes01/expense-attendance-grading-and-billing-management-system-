# for each scenario below,write which structure (list/tuple/set/dict) fits best ,and why:
#1. storing 50 students' exam scores, in the order they took the exam
scores=[85,92,78,90,88]
print(scores)
#list is best because it maintains order and can be changed.
#2 storing a single student's (name,roll_number_ -fixed ,never changes
student=("neeraj",101)
print(student)
# tuple is best because the data is fixed and should not be changed.

#3 tracking which username have already registered (no duplicates allowed)

usernames={"neeraj","pankaj","paras","prateek"}
print(usernames)
#set is best because it does not allow duplicate values

#4 storing one employee's full profile: name,salary,department,email
employee={
    "name":"neeraj",
    "salary":40000,
    "department":"it",
    "email":"parjapatineeraj2311@gmail.com"
}
print(employee)
# dictionary is best because it stores data using key value pairs.
