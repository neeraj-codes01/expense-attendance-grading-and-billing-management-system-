name=input("enter the name of owner:")
meter=int(input("enter your meter number:"))
uc=int(input("enter the units consumed:"))
if uc<=100:
    bill=uc*2.5
elif uc>=101 and uc<=200:
    bill=(100*2.5)+((uc-100)*3.5)
elif uc>=201 and uc<=300:
    bill=(100*2.5)+((100)*3.5)+((uc-200)*4)
elif uc>400:
    bill=(100*2.5)+((100)*3.5)+(100*4)+((uc-300)*4.5)
    print(" the total bill not found")
print("the total bill be:",bill)
