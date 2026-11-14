# wap to accept multiple values in a list and store it in a single dimensional array and display it.
import numpy as np
lst=[]
size=int(input("enter the size of the array"))
for i in range(size):
    no=int(input("enter the number"))
    lst.append(no)

arr=np.array(lst)
print(arr)

def info(name,age=20):
    print(name, "is", age , "years old")
info("neeraj")