def subtract(a,b):
    return a-b
print (subtract(10,6))

score=0
def add_points(points):
    global score
    score=score+points

add_points(10)
add_points(5)
print("score",score)