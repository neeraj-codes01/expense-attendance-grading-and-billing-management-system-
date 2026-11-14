#bug1: missing return statement
def add(x,y):
    total=x+y
result=add(5,3)
print(result)
#bug2: wrong number of arguments
def greet (name):
    return "hello,"+name
#greet("alice","bob") # typeerror: greet() takes 1 positional arguments but were given
#fixes:
def add(x,y):
    total=x+y
    return total
greet("alice")