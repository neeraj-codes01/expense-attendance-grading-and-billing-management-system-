# broken: forget print() after the inner loop ,so everything run together on one line
'''for row in range(5):
    for col in range(5):
        print("*",end=" ")
# missing print() here-- rows never separate'''

#fixed:
for row in range(3):
    for col in range(9):
        print("*",end=" ")
    print()#newline stored after each row


