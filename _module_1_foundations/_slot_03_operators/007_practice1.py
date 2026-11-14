# write a program to accept time in hours minutes and second and convert in second
hours=int(input("enter hours:"))
minutes=int(input("enter minutes:"))
second=int(input("enter seconds:"))
total_second=(hours*3600)+(minutes*60)+(second)
print("total time in seconds:",total_second)