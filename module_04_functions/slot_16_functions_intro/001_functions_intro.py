#write a program to design a non parameterized and non returned type function named namakaran(),
#task is to print "hello world"
def namakran():
    print("hello world")
namakran()

def greet(name):
    message="hello" +name+ "!"
    return message

print(greet("alice"))
print(greet("bob"))