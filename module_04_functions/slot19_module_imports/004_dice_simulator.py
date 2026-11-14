import random
def roll_dice():
    """"simulation rolling a 6_sided die"""
    return random.randint(1,6)
for i in range(5):
    print("roll:",roll_dice())