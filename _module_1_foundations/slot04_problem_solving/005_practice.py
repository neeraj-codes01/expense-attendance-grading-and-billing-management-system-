quantity=int(input("enter the quantity:"))
price=float(input("enter the price:"))
sales=quantity*price
if(sales>100000):
    commission=sales*10/100
elif((sales>70000)and(sales<100000)):
    commission=sales*7/100
elif((sales>40000)and(sales<70000)):
    commission=sales*4/100
elif(sales<40000):
    commission=0
else:
    print("no commission")

print("total sales:",sales)
print("commission:",commission)

#wac to accept quantity and price of laptop and that is sold by sales person where the company gives comission
# based om total sales were tariff 1.if sales more than 1 lakh 10% comission of total sales
# if sales is more than 70000 but less than 1 lakh 7% of total sales
# if sales is more than 40000 is less than comission 4%
#if sales is less than 40000 no comission


