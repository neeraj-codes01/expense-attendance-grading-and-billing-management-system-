# bug1: trying to modify a tuple
#point=(10,20)
#point[0]=15  # typeerror: 'tuple' object does not support item assignment

#bug2: assuming a set keep insertion order (it doesn't!)
#numbers={5,1,3,2,4}
#print(numbers)# order is not guaranteed to be 5,1,3,2,4-- don't rely on it
#fixes:
point=(10,20)
new_point=(15,point[1])
print(new_point)

numbers=[5,1,3,2,4]
numbers.sort()
print(numbers)
