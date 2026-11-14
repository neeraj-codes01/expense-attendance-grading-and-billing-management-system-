# bug1: trying to access a local variable outside its function
#from unittest import result
def calculate():
    result=10*5
    return result
calculate()
#print result() # nameerror: result is local to calculate(),not defined here
#bug2: forgetting 'global' when modifying a global variable inside a function
total=0
def add_to_total(amount):
    total=total+amount# unbound local error! python thinks this is a new local variable
    #fixes:
def calculate():
    result=10*5
    return result
value=calculate()
print(value)

total=0
def add_to_total(amount):
    global total
    total=total+amount