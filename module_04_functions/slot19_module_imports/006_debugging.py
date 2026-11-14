#bug1: forgetting to import the module before using it
#print(math.sqrt(16)) # nameerror: name math is not defined

#bug2:misspelling a function name (attribute error)
#import math
#print(math.squareroot(16)) # attributerror:module 'math' has no attribute 'squareroot'
#fixes:
import math
print(math.sqrt(16))#bug1: fixed import before use
print(math.sqrt(16))#bug2: correct function name is sqrt,not squareroot