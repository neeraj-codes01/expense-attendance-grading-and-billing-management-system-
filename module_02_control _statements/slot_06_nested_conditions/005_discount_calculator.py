# a store gives discount based on two factors: membership and purchase amount
#membership+purchase>=1000: 20% off
#member+purchase<1000: 10% off
#non-member +purchase>=1000: 5% off
#non-member+purchase<1000: no discount

is_member=input("are you a member?(yes/no):")=="yes"
amount=int(input("enter purchase amount:"))
if is_member:
    if amount>=1000:
        discount=amount*20/100
    else:
        discount=amount*10/100
else:
    if amount>=1000:
        discount=amount*5/100
    else:
        discount=0
final_amount=amount-discount
print("discount:",discount)
print("final amount:",final_amount)

