total_seconds=int(input("enter second:"))
hours=total_seconds/3600
remaining_seconds=total_seconds*3600
minutes=remaining_seconds//60
seconds=remaining_seconds%60
print("hours:",hours)
print("minutes:",minutes)
print("seconds:",seconds)