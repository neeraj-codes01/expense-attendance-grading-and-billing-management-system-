# wrong: 'need to get license' also prints for user under 18
#because it's nested at the wrong level
age=15
has_license=False
if age>=18:
    print("old enough")
if has_license:
    print("can drive")
print("need to get license") # bug: print even though age<18

# fixed: nest has_license check inside the age check
if age>=18:
    if has_license:
        print("can drive")
    else:
        print("neet to get license")
else:
    print("too young to drive")
