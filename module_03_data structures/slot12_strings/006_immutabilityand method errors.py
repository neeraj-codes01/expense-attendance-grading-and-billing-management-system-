#bug1: trying to change a string in place
# name="alice"
# name[0]="b"  #typeerror: str obj does not support item assignment

#bug2: forgetting string method return a new string (dont modify in place)
text="hello"
text.upper()#this does not change text!
print(text)# still prints "hello", not "HELLO"

#fixes:
name="alice"
name="B"+name[1:]  # bug1 fixed :build a new string
print(name)

text="hello"
text=text.upper()
print(text)