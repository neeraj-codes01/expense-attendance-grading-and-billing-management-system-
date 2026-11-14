from typing import cast

price=(float(input("enter price:")))
quantity=int(input("enter quantity:"))

total=price*quantity
print("the price of  my favorite number is:",total)
discount=20

if total>500:
         print("final_price",total-discount)

     # build a small program from scratch using the six step framework:
 #given the price and the quantity of an item ,calculate the total cost and apply a flat rs.20 discounts if the total if the total exceeds rs.500."
#write understand/breakdown/plan as comments,then code it.
#(conditions aren't taught until slot 5- its fine to just calculate total and print it; the discount logic return inm slot 5'''


