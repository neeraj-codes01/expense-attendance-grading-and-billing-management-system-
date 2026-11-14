#bug 1: off-by-one (range should be range(6) to include 5)
#for i in range(5):
 #   print(i) # prints 0-4,missing 5
#bug 2: accumulator not initialized
# for i in range(1,6):
# total=total+i  #Nameerror:total not defined (should initialized to 0 first)
# bug3:wrong range direction
#for i in range(10,1):  # this doesn't print anything!(10 to 1 is backwards)
 #   print(i)

#fixes:
for i in range(6):
    print(i)
total=0
for i in range(1,6):
    total=total+i
    print(i)

for i in range(10,0,-1):
    print(i)