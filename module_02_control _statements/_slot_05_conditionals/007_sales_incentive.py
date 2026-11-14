rate=int(input("enter rate:"))
qty=int(input("enter qty:"))
total=qty*rate
if total > 0:
    print("total sales:",total)
    if total>=100000:
        print("the total incentive collected is",(total*0.1))
    elif total>=70000 and total<=100000:
        print("the total incentive collected is",(total*0.07))
    elif total>=40000 and total<=700000:
        print("the total incentive collected is, (total*0.04")
    elif total<40000:
        print("the total incentive collected is",(total*0))
    else:
        print("something is not right")