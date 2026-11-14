# ask the user for a marks one at a time and store them in a list
lst=[]
print(lst)
for i in range(5):
    marks=int(input("enter your marks:"))
    lst.append(marks)
print(lst)
print(type(lst))
print(max(lst))
print(min(lst))
print(sum(lst))
print(sorted(lst))
print(reversed(lst))