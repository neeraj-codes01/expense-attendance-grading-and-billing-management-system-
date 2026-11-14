# ask for 5 student marks in a loop,store them,then print all+ the total
marks=[]
for i in range(5):
    m=int(input("enter marks:"))
    marks.append(m)
print("all marks:",marks)
print("total:",sum(marks))