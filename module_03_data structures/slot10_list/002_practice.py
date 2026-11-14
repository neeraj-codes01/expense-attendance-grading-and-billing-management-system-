# write a program to accept n number values in a list and print all even numbers and count all odd numbers
size=int(input("enter the size of the list:"))
lst=[]
ctr=0
for i in range(size):
    num=int(input("enter the number:"))
    lst.append(num)
print(lst)
#even numbers
for i in range(size): # indexing values are fetched
    if lst[i]%2==0:
        print(lst[i])

# odd numbers
for i in lst: # no used of range function (it will fetch values not index), now it will take elements in the lst
    if i%2==0:
        ctr+=1
print(ctr)

# write a program of values in a list and ask the user to which value has to be removed. remove all its instances.
# write a program to accept n number of users from a teacher then accept name and marks parallely and display
#all the students name those who have passed the exams and passing marks in 85.



