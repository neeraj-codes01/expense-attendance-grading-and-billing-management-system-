def calculate_area(length,width):
    return length*width

def calculate_perimeter(length,width):
    return 2*(length+width)
l=float(input("enter length:"))
w=float(input("enter width:"))
print("area:",calculate_area(l,w))
print("perimeter:",calculate_perimeter(l,w))


