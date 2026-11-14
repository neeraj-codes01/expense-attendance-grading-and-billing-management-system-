#broken:forget to convert before multiplication
price=input("enter price:")
quantity=input("enter quantity:")
#total=price*quantity #typeerror- is result: string repeated, not multiplied correctly

#fixed
total=int(price)*int(quantity)
print("total:",total)