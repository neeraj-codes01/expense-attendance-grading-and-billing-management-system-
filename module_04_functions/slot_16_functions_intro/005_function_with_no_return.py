def print_info(name,age):
    print(f"name: {name}, age: {age}")
print_info("alice",22)
print_info("bob",30)
#notice: calling print_info does not give you a usable return value
result=print_info("alice",22)
print(result)